from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    '''for using email as unique identifier instead of username '''

    def create_user(self, email, password, is_active=True, is_staff=False, is_superuser=False,first_name=None,last_name=None,phone=None):

        # create and save user with email and password

        if not email:
            raise ValueError('The EMail must be set ')

        if not password:
            raise ValueError('Password is mandatory')


        User = self.model(
            email=self.normalize_email(email)
        )
        User.active = is_active
        User.staff = is_staff
        User.superuser = is_superuser
        User.set_password(password)
        User.first_name=first_name
        User.last_name=last_name
        User.phone=phone
        User.save(using=self.db)
        return User

    def create_staffuser(self, email, password):
        User = self.create_user(
            email, 
            password=password, 
            is_staff=True
            )
        return User

    # def create_superuser(self,email,password=None):

    #     #create and save superuser with email and password
    #     extra_fields.setdefault('is_staff',True)
    #     extra_fields.setdefault('is_superuser',True)
    #     extra_fields.setdefault('is_active',True)

    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError(('Superuser must have have is_staff=True.'))

    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError(('Superuser must have is_superuser=True'))

    #     return self.create_user(email, password,**extra_fields)

    def create_superuser(self, email, password):
        User = self.create_user(
            email,
            password=password,
            is_staff=True, 
            is_superuser=True
            )
        return User
