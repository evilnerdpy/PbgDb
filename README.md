# PbgDb
script, which allow you to encode different files into Images

pip install pillow 
pip install numpy  are required before start
png_db = PbgDb()

png_db.encode(file_path , data_base_path)

png_db.decode(data_base_path, decoded_file_name)  # extenion necessarily

