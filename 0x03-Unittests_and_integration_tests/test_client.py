#!/usr/bin/env python3
"""Unittest module"""
import unitttest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized

from client import GitHubOrgClient


class TestGitHubOrgClient(unittest.TestCase):
    """Tests GitHubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """tests correct output"""
        endpoitn = 'https://api.github.com/orgs/{}'.format(org_name)
        spec = GitHubOrgClient(data)
        spec.org()
        mock_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'https://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """test returns correct output"""
        with patch('client.GitHubOrgClient.org',
                   PropertMock(return_value=result)):
            response = GitHubOrgClient(namr)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))
