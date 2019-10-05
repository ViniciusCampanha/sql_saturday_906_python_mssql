
-- Verifica espaço em disco
DROP TABLE #TEMP_DISK
GO
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
--WITH RESULT SETS (("device" VARCHAR(100), "total" DECIMAL(18,2), "percent" DECIMAL(18,2), "free" DECIMAL(18,2), "used" DECIMAL(18,2)))

SELECT 
	Device AS DEVICE
	,CAST(Total/1024/1024 AS DECIMAL(10,2)) AS TOTAL
	,CAST(Space_Free/1024/1024 AS DECIMAL(10,2)) AS SPACE_FREE
	,CAST(Usage/1024/1024 AS DECIMAL(10,2)) AS SPACE_USAGE
	,Percent_Usage AS PERCENT_USAGE
FROM #TEMP_DISK

-- Verificando conexao com a internet
EXECUTE sp_execute_external_script @language = N'Python'
, @script = N'
import requests

def connected_to_internet(url=''http://www.google.com/'', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("Sem conexão com a internet.")
    return False
'

-- Tentando comunicacao com outro servidor
EXECUTE sp_execute_external_script @language = N'Python'
, @script = N'
import socket

def telnet_test(ip, port):

	print("Opening connection on %s port %s", ip, str(port))

	try:
		conn=socket.create_connection((ip,port),timeout=30)
	except socket.timeout:
		print("Connection error: timeout")
		exit(-1)
	except:
		print("Connection error: unknown")
		exit(-1)
	print("Connection succeed")
	exit(0)

telnet_test("127.0.0.1",1433)
'

