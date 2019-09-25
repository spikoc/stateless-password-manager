"""
    Test the configuration parameters for the different environments (development, testing and
production).
"""
import os

from flask_testing import TestCase

from project import create_app


class DevelopmentConfigTest(TestCase):
    """Test the development environment settings."""

    def create_app(self):
        return create_app(settings='project.config.DevelopmentConfig')

    def test_app_name(self):
        """test the application name is correct"""
        self.assertEqual(os.getenv('APP_NAME', 'stateless-password-manager'),
                         self.app.config.get('APP_NAME'))

    def test_debug_enabled(self):
        """test debug mode is enabled"""
        self.assertTrue(self.app.config.get('DEBUG'))

    def test_debug_toolbar_enabled(self):
        """test debug toolbar is enabled"""
        self.assertTrue(self.app.config.get('DEBUG_TB_ENABLED'))

    def test_debug_toolbar_intercept_redirects(self):
        """test intercept does not redirect"""
        self.assertFalse(self.app.config.get('DEBUG_TB_INTERCEPT_REDIRECTS'))

    def test_env(self):
        """test what environment the app is running in"""
        self.assertEqual('development', self.app.config.get('ENV'))

    def test_secret_key(self):
        """test the secret key value is valid"""
        self.assertEqual(os.getenv('SECRET_KEY', '77c84dc23ad11ebd1e78e80acf73ce8a'),
                         self.app.config.get('SECRET_KEY'))

    def test_testing_disabled(self):
        """test testing mode is disabled"""
        self.assertFalse(self.app.config.get('TESTING'))

    def test_wtf_csrf_disabled(self):
        """test CSRF protection is disabled"""
        self.assertFalse(self.app.config.get('WTF_CSRF_ENABLED'))


class TestingConfigTest(TestCase):
    """Test the testing environment settings."""

    def create_app(self):
        return create_app(settings='project.config.TestingConfig')

    def test_app_name(self):
        """test the application name is correct"""
        self.assertEqual(os.getenv('APP_NAME', 'stateless-password-manager'),
                         self.app.config.get('APP_NAME'))

    def test_debug_disabled(self):
        """test debug mode is disabled"""
        self.assertFalse(self.app.config.get('DEBUG'))

    def test_debug_toolbar_disabled(self):
        """test debug toolbar is disabled"""
        self.assertFalse(self.app.config.get('DEBUG_TB_ENABLED'))

    def test_env(self):
        """test what environment the app is running in"""
        self.assertEqual('production', self.app.config.get('ENV'))

    def test_secret_key(self):
        """test the secret key value is valid"""
        self.assertEqual(os.getenv('SECRET_KEY', '77c84dc23ad11ebd1e78e80acf73ce8a'),
                         self.app.config.get('SECRET_KEY'))

    def test_testing_enabled(self):
        """test testing mode is enabled"""
        self.assertTrue(self.app.config.get('TESTING'))

    def test_wtf_csrf_disabled(self):
        """test CSRF protection is disabled"""
        self.assertFalse(self.app.config.get('WTF_CSRF_ENABLED'))


class ProductionConfigTest(TestCase):
    """Test the production environment settings."""

    def create_app(self):
        return create_app(settings='project.config.ProductionConfig')

    def test_app_name(self):
        """test the application name is correct"""
        self.assertEqual(os.getenv('APP_NAME', 'stateless-password-manager'),
                         self.app.config.get('APP_NAME'))

    def test_debug_disabled(self):
        """test debug mode is disabled"""
        self.assertFalse(self.app.config.get('DEBUG'))

    def test_debug_toolbar_disabled(self):
        """test debug toolbar is disabled"""
        self.assertFalse(self.app.config.get('DEBUG_TB_ENABLED'))

    def test_env(self):
        """test what environment the app is running in"""
        self.assertEqual('production', self.app.config.get('ENV'))

    def test_secret_key(self):
        """test the secret key value is valid"""
        self.assertEqual(os.getenv('SECRET_KEY', '77c84dc23ad11ebd1e78e80acf73ce8a'),
                         self.app.config.get('SECRET_KEY'))

    def test_testing_disabled(self):
        """test testing mode is disabled"""
        self.assertFalse(self.app.config.get('TESTING'))

    def test_wtf_csrf_enabled(self):
        """test CSRF protection is enabled"""
        self.assertTrue(self.app.config.get('WTF_CSRF_ENABLED'))
