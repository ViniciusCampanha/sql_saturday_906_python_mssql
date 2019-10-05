USE DBA
GO

ALTER PROCEDURE WebHookAlertToSlack @message_txt VARCHAR(4000)
AS
BEGIN

declare @webhook varchar(4000) = 'https://hooks.slack.com/services/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'

EXEC sp_execute_external_script @language =N'Python',
@script=N'
import json
import urllib3

urllib3.disable_warnings()
http = http = urllib3.PoolManager()

def post_to_slack(message):
    slack_url = "https://hooks.slack.com/services/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"
    
    encoded_data = json.dumps({''text'': message, ''username'': "SQL Server", "icon_url": "" })
    response = http.request("POST", slack_url, body=encoded_data, headers={''Content-Type'': ''application/json''})
    
post_to_slack(message_txt_in)
',
@params = N'@message_txt_in varchar(4000)',
@message_txt_in = @message_txt
END 
GO

ALTER PROCEDURE AlertaEspacoDisco
AS
BEGIN

	DECLARE @mensagem_alerta varchar(4000)
			, @percentage_usage INT
			, @webhook varchar(4000) = 'https://hooks.slack.com/services/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'

	CREATE TABLE #TEMP_DISK(
		Device VARCHAR(100)
		,Total DECIMAL(18,2)
		,Percent_Usage DECIMAL(18,2)
		,Space_Free DECIMAL(18,2)
		,Usage DECIMAL(18,2)
	)

	-- Capturando dados de utilização de disco do sistema operacional
	INSERT INTO #TEMP_DISK(Device, Total, Percent_Usage, Space_Free, Usage) 
	EXECUTE sp_execute_external_script @language = N'Python'
, @script = N'
import psutil
import pandas as pd

result_usage = psutil.disk_usage(".")

for part in psutil.disk_partitions(all=False):
	usage = psutil.disk_usage(part.mountpoint)
	s = {"device":[part.device],"total":[usage.total], "used": [usage.used], "free":[usage.free], "percent":[int(usage.percent)]}

df = pd.DataFrame(s)

OutputDataSet = df

'
	, @input_data_1 = N''
	, @output_data_1_name = N'OutputDataSet'

	SELECT 
		Device AS DEVICE
		,CAST(Space_Free/1024/1024 AS DECIMAL(10,2)) AS TOTAL
		,CAST(Total/1024/1024 AS DECIMAL(10,2)) AS SPACE_FREE
		,CAST(Usage/1024/1024 AS DECIMAL(10,2)) AS SPACE_USAGE
		,Percent_Usage AS PERCENT_USAGE
	FROM #TEMP_DISK

	SELECT @percentage_usage = CAST(Percent_Usage AS INT) FROM #TEMP_DISK

	IF @percentage_usage > 80
	BEGIN

		SET @mensagem_alerta = 'Alerta de espaco em disco menor a 80% no servidor: ' + CAST(@@SERVERNAME AS vARCHAR(100)) + '.'
		select @mensagem_alerta

		EXEC WebHookAlertToSlack @message_txt = @mensagem_alerta

	END

END
GO

-- Testando 

exec AlertaEspacoDisco
EXEC WebHookAlertToSlack @message_txt = 'Alerta de espaco em disco no servidor'
