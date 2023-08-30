import pytest
from linked_list import LinkedList

@pytest.fixture
def empty_linked_list():
    return LinkedList()

@pytest.fixture
def populated_linked_list():
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    return llist

def test_append(empty_linked_list):
    empty_linked_list.append(1)
    assert empty_linked_list.length() == 1

def test_length(populated_linked_list):
    assert populated_linked_list.length() == 3

def test_display(populated_linked_list, capsys):
    populated_linked_list.display()
    captured = capsys.readouterr()
    assert captured.out == "[1, 2, 3]\n"

def test_get(populated_linked_list):
    assert populated_linked_list.get(0) == 1
    assert populated_linked_list.get(1) == 2
    assert populated_linked_list.get(2) == 3

def test_get_out_of_range(populated_linked_list, capsys):
    populated_linked_list.get(3)
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Index out of range\n"

def test_erase(populated_linked_list):
    populated_linked_list.erase(1)
    assert populated_linked_list.length() == 2
    assert populated_linked_list.get(0) == 1
    assert populated_linked_list.get(1) == 3

def test_erase_out_of_range(populated_linked_list, capsys):
    populated_linked_list.erase(3)
    captured = capsys.readouterr()
    assert captured.out == "ERROR: Index out of range\n"
