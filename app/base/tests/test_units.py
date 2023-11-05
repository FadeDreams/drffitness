"""
Tests for models.
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from base import models


class ModelTests(TestCase):
    """Test models."""

    def test_function_1(self):
        """Test creating a user with an email is successful."""
        email = 't@e.com'
        password = 'passpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_function_2(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['aaa1@EXAMPLE.com', 'aaa1@example.com'],
            ['bbb2@Example.com', 'bbb2@example.com'],
            ['vvv3@EXAMPLE.com', 'vvv3@example.com'],
            ['ddd4@example.COM', 'ddd4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_function_3(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_function_4(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

