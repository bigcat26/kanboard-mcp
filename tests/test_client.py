"""Integration tests for KanboardClient.call_api method."""

import pytest
from dotenv import load_dotenv

from kanboard_mcp.config import Config
from kanboard_mcp.client import KanboardClient

# Load environment variables from .env file
load_dotenv()


@pytest.fixture
def client():
    """Create a KanboardClient instance from environment configuration."""
    config = Config.from_env()
    return KanboardClient(config)

def test_call_api_get_me(client):
    """Test call_api with getMe method."""
    result = client.call_api("getMe")
    assert isinstance(result, dict)

def test_call_api_get_all_projects(client):
    """Test call_api with getAllProjects method."""
    result = client.call_api("getAllProjects")
    assert isinstance(result, list)

def test_call_api_get_all_tasks(client):
    """Test call_api with getAllTasks method."""
    # result = client.call_api("getAllTasks", project_id=1)
    result = client.call_api("getAllTasks", project_id=1)
    assert isinstance(result, list)

def test_call_api_get_overdue_tasks_by_project(client):
    """Test call_api with getOverdueTasksByProject method."""
    result = client.call_api("getOverdueTasksByProject", project_id=1)
    assert isinstance(result, list)

def test_call_api_get_project_by_id(client):
    """Test call_api with getProjectById method."""
    result = client.call_api("getProjectById", project_id=1)
    assert isinstance(result, dict)
    assert "id" in result
    assert "name" in result

def test_call_api_get_project_by_name(client):
    """Test call_api with getProjectByName method."""
    result = client.call_api("getProjectByName", name="Project")
    assert isinstance(result, dict)
    assert "id" in result
    assert "name" in result


def test_call_api_get_columns(client):
    """Test call_api with getColumns method."""
    result = client.call_api("getColumns", project_id=1)
    assert isinstance(result, list)
    if result:
        assert isinstance(result[0], dict)
        assert "id" in result[0]


def test_call_api_get_task_by_reference(client):
    """Test call_api with getTaskByReference method."""
    result = client.call_api("getTaskByReference", project_id=1, reference="REF-123")
    if result is not None:
        assert isinstance(result, dict)
        assert "id" in result


def test_call_api_get_all_categories(client):
    """Test call_api with getAllCategories method."""
    result = client.call_api("getAllCategories", project_id=1)
    assert isinstance(result, list)
    if result:
        assert isinstance(result[0], dict)
        assert "id" in result[0]


def test_call_api_get_project_activities(client):
    """Test call_api with getProjectActivities method."""
    result = client.call_api("getProjectActivities", project_ids=[1])
    assert isinstance(result, list)
    if result:
        assert isinstance(result[0], dict)
        assert "event_name" in result[0]
