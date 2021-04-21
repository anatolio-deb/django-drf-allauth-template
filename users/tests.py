from django.test import TestCase

from users.forms import CustomSignupForm
from users.models import CustomUser, CustomUserManager

USER = dict(name="Bob", email="bob@example.com", password="some_password")


class TestClass01(TestCase):
    """CustomUser instance created properly"""

    @classmethod
    def setUpClass(cls) -> None:
        """Created an instance to test"""
        super().setUpClass()
        cls.user = CustomUser.objects.create(
            email=USER["email"],
            name=USER["name"],
        )

    def test_case01(self):
        """Instance's created"""
        self.assertTrue(CustomUser.objects.filter(email=USER["email"]).exists())

    def test_case02(self):
        """Instance's active (is_active)"""
        self.assertTrue(self.user.is_active)

    def test_case03(self):
        """Instance's not staff (is_staff)"""
        self.assertFalse(self.user.is_staff)

    def test_case04(self):
        """Instance's __str__ -> instance.email"""
        self.assertEqual(self.user.__str__(), USER["email"])


class TestClass02(TestCase):
    """CustomSignup form initializes properly"""

    def setUp(self) -> None:
        """Initialize a form"""
        self.form = CustomSignupForm(
            data={
                "name": USER["name"],
                "email": USER["email"],
                "password1": USER["password"],
                "password2": USER["password"],
            }
        )

    def test_case01(self):
        """CustomSignup form is valid"""
        self.assertTrue(self.form.is_valid())


class TestClass03(TestCase):
    """CustomUserManager"""

    def setUp(self) -> None:
        """Instansiate CustomSignup"""
        self.manager = CustomUserManager()
        self.manager.model = CustomUser

    def test_case01(self):
        """Create superuserperuser normal"""
        superuser = self.manager.create_superuser(email=USER["email"], name=USER["name"], password=USER["password"])
        self.assertTrue(CustomUser.objects.filter(email=USER["email"]).exists())
        self.assertTrue(isinstance(superuser, CustomUser))
        self.assertEqual(superuser.email, USER["email"])
        self.assertEqual(superuser.name, USER["name"])
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_case02(self):
        """Create superuserperuser without required parameter (email)"""
        with self.assertRaises(ValueError):
            self.manager.create_superuser(email="", name=USER["name"], password=USER["password"])
