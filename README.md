This is an exercise for practicing availability patterns architectural, specially redundant spare pattern.
This exercise is designed based on "Software Architecture in Practice" book, intended to use in software architecture classes.
persian documentation is available in the repository.
## how to install:

1. clone the repo

    ```bash
    git clone https://github.com/mohamad-khorsandi/redundant-spare-practice.git
    cd redundant-spare-practice   
    ```

2. create a virtual enviroment(optional)

3. install requirements

   ```bash
   pip install -r requirements.txt
   ```

4. run proxy

    ```bash
    cd proxy
    python proxy.py 8000
    ```

5. run server

    ```bash
    cd server
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 8001
    ```

6. run spare

    ```bash
    cd spare
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 8002
    ```

7. open your browser and type http://127.0.0.1:8000 to see the main page. 

8. you can use monitor page to test how systems behaves when one or two servers are down

<img width="498" height="284" alt="Screenshot 2025-07-13 210003" src="https://github.com/user-attachments/assets/eace466a-ccbd-464c-874e-e34d7eb0e4ab" />

