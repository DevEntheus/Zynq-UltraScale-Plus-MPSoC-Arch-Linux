# BASE ADDRESSES
BASE_ADDR = 0x8000_0000; REGION_SIZE = 0x2000_0000  # 512M bytes

SANITY_TEST = '''
      _/_/_/    _/_/    _/      _/  _/_/_/  _/_/_/_/_/  _/      _/      _/_/_/_/_/  _/_/_/_/    _/_/_/  _/_/_/_/_/   
   _/        _/    _/  _/_/    _/    _/        _/        _/  _/            _/      _/        _/            _/        
    _/_/    _/_/_/_/  _/  _/  _/    _/        _/          _/              _/      _/_/_/      _/_/        _/         
       _/  _/    _/  _/    _/_/    _/        _/          _/              _/      _/              _/      _/          
_/_/_/    _/    _/  _/      _/  _/_/_/      _/          _/              _/      _/_/_/_/  _/_/_/        _/          
'''

PASSED = '''\n                                                  
    _/_/_/      _/_/      _/_/_/    _/_/_/  _/_/_/_/  _/_/_/    
   _/    _/  _/    _/  _/        _/        _/        _/    _/   
  _/_/_/    _/_/_/_/    _/_/      _/_/    _/_/_/    _/    _/    
 _/        _/    _/        _/        _/  _/        _/    _/     
_/        _/    _/  _/_/_/    _/_/_/    _/_/_/_/  _/_/_/        
'''

FAILED = '''\n                                                
    _/_/_/_/    _/_/    _/_/_/  _/        _/_/_/_/  _/_/_/    
   _/        _/    _/    _/    _/        _/        _/    _/   
  _/_/_/    _/_/_/_/    _/    _/        _/_/_/    _/    _/    
 _/        _/    _/    _/    _/        _/        _/    _/     
_/        _/    _/  _/_/_/  _/_/_/_/  _/_/_/_/  _/_/_/        
'''