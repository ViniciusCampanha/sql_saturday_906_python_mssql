import docker

def start_sql_instance():
    
    connection = docker.from_env()
    #cli = Client(base_url='tcp://127.0.0.1:2375')

    sqlcontainer = connection.containers.run(
        "mcr.microsoft.com/mssql/server:2019-RC1.0-ubuntu",
        detach = True,
        environment = ["ACCEPT_EULA=Y","SA_PASSWORD=P@ssW0rd"],
        ports = {'1435/tcp': 1433},
        name = 'SQLContainer',
    )

    #cli.containers()

    print(sqlcontainer.logs())


start_sql_instance()