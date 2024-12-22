from pydantic_settings import BaseSettings
# BaseSettings allows values to be overridden by environment variables.

class Settings(BaseSettings):
    # Use the appropriate data from the .env file
    database_username :str
    database_password :str
    database_host :str  
    database_port :str   
    database_name :str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    
    
    class Config:
        env_file = ".env"  

# Initialize settings
settings = Settings()




 
 




