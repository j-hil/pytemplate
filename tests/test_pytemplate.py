from pytemplate import __version__, __author__

def test_metadata():
    assert isinstance(__version__, str)
    assert isinstance(__author__, str)