import pytest
import youtube_find_info_def as y


def test_get_view_count():
    # for el in y.get_view_count(y.adele_list):
    #     x = el[view].split() 
    #     assert float(x[0]) > 5 and v[1] == 'млрд'
    assert y.get_view_count(y.adele_list)
    
if __name__ == '__main__':
    pytest.main()   
