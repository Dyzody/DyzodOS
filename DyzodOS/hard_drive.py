import os

import graphics_driver
import data_tools
import settings

DELIMITER = data_tools.GetDataType(Inp=settings.DELIMITER, OutputType="string")
OS_HDD_FOLDER = os.path.join(os.path.dirname(__file__), "os_hdd")

def Create() -> None:
    os.makedirs(OS_HDD_FOLDER, exist_ok=True)
    graphics_driver.WriteLn("OS HDD folder created successfully")

def EncryptString(String) -> str:
    Inp_Bytes = data_tools.GetDataType(Inp=String, OutputType="bytes")
    Encrypted_Bytes = settings.OS_FERNET.encrypt(Inp_Bytes)
    Output_String = data_tools.GetDataType(Inp=Encrypted_Bytes, OutputType="string")
    return Output_String
    #return data_tools.GetDataType(Inp=String, OutputType="string")#settings.OS_FERNET.encrypt(String.encode()).decode()

def DecryptString(String) -> str:
    Inp_Bytes = data_tools.GetDataType(Inp=String, OutputType="bytes")
    Decrypted_Bytes = settings.OS_FERNET.decrypt(Inp_Bytes)
    Output_String = data_tools.GetDataType(Inp=Decrypted_Bytes, OutputType="string")
    return Output_String
    #return data_tools.GetDataType(Inp=String, OutputType="string")#settings.OS_FERNET.decrypt(String.encode()).decode()

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

def GetClusterLen(Name) -> int:
    file_path = os.path.join(OS_HDD_FOLDER, f"{Name}.bin")
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            return len(file.read())

def GetClusterByName(Name) -> str:
    file_path = os.path.join(OS_HDD_FOLDER, f"{Name}.bin")
    if os.path.exists(file_path) and GetClusterLen(Name) > 0:
        with open(file_path, "rb") as file:
            return DecryptString(file.read())
        
def GetHddContent() -> str:
    content = ""
    for file_name in os.listdir(OS_HDD_FOLDER):
        # with open(os.path.join(OS_HDD_FOLDER, file_name), "rb") as file:
            # file_content = (DecryptString(file.read()))
            # content += file_content + DELIMITER
        content += GetClusterByName(file_name.strip(".bin"))

    return content.strip(DELIMITER)

def WriteToCluster(ChunkName, NewContent) -> bool:
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
