echo "Building the project..."
python3.9 -m pip install -r requirements.txt

echo "Make migration..."
python3.9 manage.py makemigrations 
python3.9 manage.py migrate 

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear