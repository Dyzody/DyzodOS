import os

import graphics_driver
import data_tools
import settings

DELIMITER = data_tools.GetDataType(Inp=settings.DELIMITER, OutputType="string")
OS_HDD_FOLDER = os.path.join(os.path.dirname(__file__), "os_hdd")

def Create() -> None:
    os.makedirs(OS_HDD_FOLDER, exist_ok=True)
    graphics_driver.WriteLn("OS HDD folder created successfully")

#Für debugging deaktiviert
def EncryptString(String) -> str:
    return data_tools.GetDataType(Inp=String, OutputType="string")#settings.OS_FERNET.encrypt(String.encode()).decode()

def DecryptString(String) -> str:
    return data_tools.GetDataType(Inp=String, OutputType="string")#settings.OS_FERNET.decrypt(String.encode()).decode()

def GetHddContent() -> str:
    encrypted_content = ""
    for file_name in os.listdir(OS_HDD_FOLDER):
        with open(os.path.join(OS_HDD_FOLDER, file_name), "rb") as file:
            encrypted_content += data_tools.GetDataType(Inp=file.read(), OutputType="string") + DELIMITER
    return encrypted_content.strip(DELIMITER)

def AddToHdd(ChunkName, Data) -> None:
    file_path = os.path.join(OS_HDD_FOLDER, f"{ChunkName}.bin")
    with open(file_path, "wb") as file:
        encrypted_data = data_tools.GetDataType(Inp=EncryptString(Data), OutputType="bytes")
        file.write(encrypted_data)

def GetClusters():
    clusters = []
    for file_name in os.listdir(OS_HDD_FOLDER):
        if file_name.endswith(".bin"):
            clusters.append(file_name[:-4])
    return clusters

def AddCluster(ChunkName, ChunkContent=""):
    AddToHdd(ChunkName, ChunkContent)

def GetClusterByName(Name):
    file_path = os.path.join(OS_HDD_FOLDER, f"{Name}.bin")
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            return data_tools.GetDataType(Inp=file.read(), OutputType="string")

def WriteToCluster(ChunkName, NewContent):
    file_path = os.path.join(OS_HDD_FOLDER, f"{ChunkName}.bin")
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            existing_content = DecryptString(data_tools.GetDataType(file.read(), "string"))
            new_content = existing_content + NewContent
        with open(file_path, "wb") as file:
            new_content_s = data_tools.GetDataType(new_content, "string")
            new_content_encrypted = EncryptString(new_content_s)
            new_content_encrypted_s = data_tools.GetDataType(new_content_encrypted, "bytes")
            file.write(new_content_encrypted_s)
            return True

if not os.path.exists(OS_HDD_FOLDER):
    Create()
