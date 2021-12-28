import pytest
from unittest.mock import Mock, patch


class AuthMock:
    @pytest.fixture
    def auth_mock(self):
        with patch("project.tools.security.auth_check") as mock:
            mock.return_value = True
            yield mock
