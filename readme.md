python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
pip freeze > requirements.txt

feature to be add

1.  blog  view for home page
   1.1 blog model (b_id,b_title,b_content,b_status,u_id,time)
   1.2  api to fetch random blog (api/home)
   1.3  what should it return  
        1.3.1  id,title,time (opt. user)
        1.3.2 only 5
   1.4 in click on particulra blog (api/home/<name:title> or <int:number>)
        1.4.1 on click get the blog details from db 
