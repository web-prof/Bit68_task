endpoints:
1-registerations endpoint:  http://127.0.0.1:8000/accounts/register/
2-post/get_products_endpoint:  http://127.0.0.1:8000/products/
3-searching through the products using username endpoint:  http://127.0.0.1:8000/products/?search=username_required_startswith
4-update/get/delete_products_endpoint: http://127.0.0.1:8000/products/user_id
4-login using djangosimplejwt to get access and refresh tokens endpoint: http://127.0.0.1:8000/api/token/

dependenciese: 
please install the requirements.txt file using (pip install -r requirements.txt) command on cmd

system requirements:
1- os windows
2-as celery is used as an extra to provide some periodic tasks on redis-server
    which isn't compitable with windows 
    the file named Ad-Aware96Install.msi located in src/redis/Ad-Aware96Install.msi must be 
    installed if testing the feature is reuqired
    **consider using these commands on different cmd windows inaddtion to the ordinary run_server cmd window:
            celery -A project.celery beat  -l info
            celery -A project.celery --pool=solo worker  -l info  
        
notes:
1-all products objects are ordered using price as required on the tasks requirements


