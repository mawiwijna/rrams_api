from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.templating import Jinja2Templates
from typing import Optional, List
import logging

from fastapi.responses import HTMLResponse
import psycopg2
from psycopg2.extras import RealDictCursor
import uvicorn

from models.themodel import ModelaPost1
from fastapi.middleware.cors import CORSMiddleware

apprrams2023b = FastAPI()
templates = Jinja2Templates(directory="templates")

origins = ["*"]

apprrams2023b.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(filename='logging-beta1000-debug-3.log', level=logging.DEBUG)
logging.basicConfig(filename='logging-beta1000-error-3.log', level=logging.ERROR)
    
print = logging.debug

# --------------------------------------------------

def set_establish_connection():
  return psycopg2.connect(dbname='dbrrams2002', user='postgres', password='asdfghjkl!@#$%^&*()_+', host='31.187.75.138', port='5432', cursor_factory=RealDictCursor)

# ------------------------------

def exec_sql(inSQL):
  cursor.execute(inSQL)
  users = cursor.fetchall()
  cursor.execute("COMMIT")
  cursor.close()
  conn.close()
  return users

def exec_sql_query1(inSQL):
  conn = psycopg2.connect(
     database="dbrrams2002",
     user="postgres",
     password="asdfghjkl!@#$%^&*()_+",
     host="localhost",
     port="5432",
     cursor_factory=RealDictCursor)
  cursor = conn.cursor()

  try:
    cursor.execute(inSQL)
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users
    
  except:
    #logging.debug(e.message)
    try:
      cursor.close()
      cursor = conn.cursor()
    except:
      conn.close()
      conn = psycopg2.connect(
        database="dbrrams2002",
        user="postgres",
        password="asdfghjkl!@#$%^&*()_+",
        host="localhost",
        port="5432",
        cursor_factory=RealDictCursor)
    cursor = conn.cursor()

def exec_sql_query2(inSQL):
  logging.debug('START-2A')
  conn = set_establish_connection()
  #cursor = conn.cursor(cursor_factory = RealDictCursor)
  logging.debug('START-2B')
  
  try:
    logging.debug('EXEC-FUN-2' + inSQL)
    cursor.execute("BEGIN")
    cursor.execute(inSQL)
    hasil = cursor.fetchall()
    cursor.execute("COMMIT")
    
    cursor.close()
    conn.close()
    return hasil
    
  except:
    #logging.debug(e.message)
    try:
      cursor.close()
      cursor = conn.cursor()
    except:
      conn.close()
      conn = set_establish_connection()
      #cursor = conn.cursor(cursor_factory = RealDictCursor)
      
    cursor = conn.cursor()

def exec_sql_query1a(inSQL):
  koneksidb = set_establish_connection()
  cursor = koneksidb.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
  
  cursor.execute(inSQL)
  hasil = cursor.fetchall()
  
  cursor.close()
  koneksidb.close()
  return hasil

def exec_sql_query2b(inSQL):
  logging.debug('START-2A')
  koneksidb = set_establish_connection()
  cursor = koneksidb.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
  logging.debug('START-2B')
  
  logging.debug('EXEC-FUN-2' + inSQL)
  #cursor.execute("BEGIN")
  cursor.execute(inSQL)
  koneksidb.commit()
  #hasil = cursor.fetchall()
  #cursor.execute("COMMIT")
  
  cursor.close()
  koneksidb.close()
  logging.debug('END-#3')
  return True
    
# --------------------------------------------------

@apprrams2023b.get("/", response_class=HTMLResponse)
async def root():
  return """
  <!doctype html>
  <html lang="en">
  <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  <title>RRAMS FAST API</title>
  </head>
  <body>
  <div class="h-100 d-flex align-items-center justify-content-center">
  <div class="alert alert-info m-5">
  RRAMS 2023 FAST API
  </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
  </body>
  </html>
    """
  #return {"message": "Hello World 12345"}


@apprrams2023b.get("/tes-upload")
def debug_tes_upload(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@apprrams2023b.get("/master_kategori1")
async def read_users():
  #users = exec_sql("SELECT * FROM tb1_master_kategori1")
  users = exec_sql("select fun1.* FROM fmx_ma_kategori_1('XN', 'u1', 'x', 'Functional RegionX', 'functional-region-x', 1) fun1")
  return {"data": users}
  
  #cursor.execute("SELECT * FROM tb1_master_kategori1")
  #users = cursor.fetchall()
  #cursor.close()
  #conn.close()
  #return {"data": users}

@apprrams2023b.post("/master_kategori1", status_code=201, response_model=ModelaPost1 )
async def read_users2(post: ModelaPost1):
  #users = exec_sql("SELECT * FROM tb1_master_kategori1")
  #users = exec_sql("select fun1.* FROM fmx_ma_kategori_1('XN', 'u1', 'x', 'Functional RegionX', 'functional-region-x', 1) fun1")
  post.id = post.id + 'DIGIMON'
  post.nama = post.nama + '_WX'
  return post

# -----

@apprrams2023b.post("/autentikasi_a101")
async def get_autentikasi_101(post: ModelaPost1):
  #vt_SQL1  = """
  #SELECT * 
  #FROM tb1_master_kategori1 
  #WHERE qa05idx = '""" + post.id +  """' 
  #"""
  
  #vd_exec1 = exec_sql(vt_SQL1)
  return {"data": {'sukses': True}}

# -----
# -----

@apprrams2023b.post("/upload_u101")
async def get_upload_umum_101(fileyy: UploadFile):
  return { "filename": fileyy.filename }

#def save_file(filename, data):
#  with open(filename, 'wb') as f:
#    f.write(data)
#    print('file saved')

@apprrams2023b.post("/upload_u102")
async def get_upload_umum_102(files: List[UploadFile] = File(...)):
  print(files)
  for file in files:
    #contents = await file.read()
    #save_file(file.filename, contents)
    print('file received')

  return {"Uploaded Filenames": [file.filename for file in files]}
    
@apprrams2023b.post("/upload_u103")
def get_upload_umum_103(namax: str = Form(...), file: UploadFile = File(...)):
  print('tree= ' + namax)
  try:
    contents = file.file.read()
    with open("uploaded_" + namax + '__' + file.filename, "wb") as f:
      f.write(contents)
  except Exception:
    return {"message": "There was an error uploading the file"}
  finally:
    file.file.close()
      
  return {"message": f"Successfuly uploaded {file.filename}"}

@apprrams2023b.post("/upload_u104")
def get_upload_umum_104(namax: str = Form(...), file: UploadFile = File(...)):
  logging.debug('rumput= ' + namax)
  from datetime import datetime
  import os
  
  vt_pk = 'fx' + datetime.utcnow().strftime('%d%H%M%S')
  
  try:
    contents = file.file.read()
    vt_filename_tosave = "uploaded_" + namax + '__' + file.filename
    
    with open(vt_filename_tosave, "wb") as f:
      f.write(contents)
    
    # -------------------------
    
    file_name1, file_extension1 = os.path.splitext(vt_filename_tosave)
  
    vt_SQL1 = """
    INSERT INTO tb3_repositori1 ( 
    qc01idx, qc01timestamplog1, qc01iduser1, qc01timestampcreated, 
    qc01filename, qc01filetype, qc01filesize, 
    qc01kategori1, qc01kategori2
    ) VALUES (
    '%s', current_timestamp, 'us01', current_timestamp,
    '%s', '%s', %d, 
    1, 1
    )
    """ % (vt_pk, file.filename, file_extension1, file.size )
    
    exec_sql_query2b(vt_SQL1)
    
    # -------------------------
    
    file_data = None
    with open(vt_filename_tosave, 'rb') as frd: 
      file_data = frd.read() 
    
    BLOB = psycopg2.Binary(file_data) 
    
    vt_SQL2 = """
    UPDATE tb3_repositori1 
    SET qc01blob1 = %s   
    WHERE qc01idx = '%s'  
    """ % (BLOB, vt_pk)
    
    exec_sql_query2b(vt_SQL2)
        
  except Exception as e:
    logging.debug('except = %s', e)
    return {"message": "There was an error uploading the file"}
  finally:
    file.file.close()
      
  return {"message": f"Successfuly uploaded {file.filename}"}

@apprrams2023b.post("/upload_list_u101")
async def get_upload_list_umum_101():
  vt_SQL1  = """
  SELECT 
  QA.qc01idx, 
  TO_CHAR(QA.qc01timestampcreated, 'YYYYMMDDHH24MISS') AS qc01timestampcreated, 
  QA.qc01filename, QA.qc01filetype, QA.qc01filesize, QA.qc01kategori1, QA.qc01kategori2  
  FROM tb3_repositori1 QA  
  ORDER BY QA.qc01timestampcreated ASC   
  """
  
  sql1 = exec_sql_query1a(vt_SQL1)
  return { "datax": sql1 }

# -----
# -----

@apprrams2023b.post("/master_kategori_u101")
async def get_master_kategori_umum_101():
  vt_SQL1  = """
  SELECT QA.* 
  FROM tb1_master_kategori1 QA  
  WHERE QA.qa05statustampil = 1 
  ORDER BY QA.qa05defnama1 ASC   
  """
  
  sql1 = exec_sql_query1(vt_SQL1)
  return { "datax": sql1 }

@apprrams2023b.get("/master_kategori_b101")
async def get_master_kategori_adminonly_101():
  sql1 = exec_sql("SELECT * FROM tb1_master_kategori1")
  return { "data": sql1 }

@apprrams2023b.post("/master_kategori_b201")
async def get_master_kategori_adminonly_201(post: ModelaPost1):
  vt_SQL1  = """
  SELECT * 
  FROM tb1_master_kategori1 
  WHERE qa05idx = '""" + post.id +  """' 
  """
  
  vd_exec1 = exec_sql(vt_SQL1)
  return {"data": vd_exec1}

# -----
  
@apprrams2023b.get("/analisisjalan_a101")
async def get_analisisjalan_umum_101(post: ModelaPost1):
  sql1 = exec_sql("SELECT * FROM tb2_analisis_jalan1 WHERE qb01statustampil = 1 ORDER BY tb2_analisis_jalan1 DESC ")
  return {"data": sql1}  

@apprrams2023b.get("/analisisjalan_a102")
async def get_analisisjalan_umum_102(post: ModelaPost1):
  vt_SQL1  = """
  SELECT * 
  FROM tb2_analisis_jalan1 
  WHERE qb01statustampil = %d 
  ORDER BY tb2_analisis_jalan1 DESC 
  """ % (post.status_tampil)
  
  vo_exec1 = exec_sql(vt_SQL1)
  return {"data": vo_exec1}  

@apprrams2023b.get("/analisisjalan_b101")
async def get_analisisjalan_adminonly_101():
  sql1 = exec_sql("SELECT * FROM tb2_analisis_jalan1 ORDER BY tb2_analisis_jalan1 DESC")
  return {"data": sql1}





  #cursor.execute(inSQL)
  #users = cursor.fetchall()
  #cursor.close()
  #conn.close()
  #return users
    
    
if __name__ == '__main__':
  uvicorn.run(apprrams2023b, port=3991, host='0.0.0.0')
  
