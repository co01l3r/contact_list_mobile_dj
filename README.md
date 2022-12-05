# contact_list_mobile
Simple contact list app. Can store and provide basic personal information, where each one except 'name' and 'note' is validated and cannot be stored invalid, however it can be left empty except 'name'. To change the default phone area code rather delete, or edit the highlighted part accordingly.

```forms.py```

![image](https://user-images.githubusercontent.com/25802489/205768497-7ef7cac7-5c95-461d-81d4-c26fa0b01f4d.png)

#### how to use:
```python
$ virtualenv <env_name>
$ source <env_name>/bin/activate
(<env_name>) $ pip install -r path/to/requirements.txt

from project folder:

(<env_name>) $ python3 manage.py runserver
```
#### create, update, delete:
![create](https://user-images.githubusercontent.com/25802489/205765317-b76bd9f8-2d66-42ff-b2b7-66867c9fd815.gif)
![details](https://user-images.githubusercontent.com/25802489/205765427-b036c09c-a20a-4d2e-8d96-fb40d831bce6.gif)
![update](https://user-images.githubusercontent.com/25802489/205765963-a278f8b2-77e5-4e78-bb29-1b5a87a2a989.gif)
![delete](https://user-images.githubusercontent.com/25802489/205766138-8d11cc83-de1a-416b-b2c2-22d674bfbc8f.gif)
#### search:
![search](https://user-images.githubusercontent.com/25802489/205766378-ec1bd7a1-b7b1-4bbf-8937-a14af07149db.gif)
#### contacts having birthday today:
![bday](https://user-images.githubusercontent.com/25802489/205766796-517e7625-c805-4346-9e5f-2e6c36a7e1c3.jpg)
