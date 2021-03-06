import base64


def iconData():
    icon = """AAABAAMAEBAAAAEAIABoBAAANgAAACAgAAABACAAKBEAAJ4EAAAwMAAAAQAgAGgmAADGFQAAKAAA
        ABAAAAAgAAAAAQAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABVVVUw
        U1NTllVVVdlUVFT5VFRU+VVVVdlTU1OWVVVVMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFVVVQlV
        VVWZVVVV/VVVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf1VVVWZVVVVCQAAAAAAAAAAAAAAAFVV
        VQlVVVXBVVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVcFVVVUJAAAA
        AAAAAABVVVWZampq/3V1df9VVVX/VVVV/2pqav93d3f/VVVV/1VVVf+JiYn/dnZ2/1VVVf9VVVX/
        VVVVmQAAAABVVVUwVVVV/ZSUlP+8vLz/VVVV/1VVVf+UlJT/wcHB/1VVVf9cXFz/9vb2/8TExP9V
        VVX/VVVV/1VVVf1VVVUwU1NTllVVVf+UlJT/urq6/2ZmZv90dHT/kpKS/8HBwf9VVVX/gYGB/9LS
        0v/m5ub/VVVV/1VVVf9VVVX/U1NTllVVVdlVVVX/lJSU/7m5uf+kpKT/ycnJ/5CQkP/BwcH/VVVV
        /6enp/+ysrL/5+fn/2RkZP9VVVX/VVVV/1VVVdlUVFT5VVVV/5SUlP+0tLT/2dnZ/9/f3/+Tk5P/
        wcHB/1VVVf/Nzc3/lJSU/8rKyv+JiYn/VVVV/1VVVf9UVFT5VFRU+VVVVf+UlJT/u7u7/9nZ2f+q
        qqr/uLi4/8HBwf9VVVX/8vLy/29vb/+oqKj/r6+v/1VVVf9VVVX/VFRU+VVVVdlVVVX/lJSU/93d
        3f+kpKT/d3d3/9vb2//BwcH/bm5u//T09P9WVlb/hYWF/9TU1P9VVVX/VVVV/1VVVdlTU1OWVVVV
        /5SUlP/7+/v/b29v/1VVVf/o6Oj/wcHB/5SUlP/Q0ND/VVVV/2NjY//39/f/V1dX/1VVVf9TU1OW
        VVVVMFVVVf2UlJT/4+Pj/1VVVf9VVVX/ubm5/8HBwf+4uLj/q6ur/1VVVf9VVVX/6enp/3R0dP9V
        VVX9VVVVMAAAAABVVVWZbm5u/4CAgP9VVVX/VVVV/25ubv+BgYH/h4eH/25ubv9VVVX/VVVV/4aG
        hv9tbW3/VVVVmQAAAAAAAAAAVVVVCVVVVcFVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVVwVVVVQkAAAAAAAAAAAAAAABVVVUJVVVVmVVVVf1VVVX/VVVV/1VVVf9VVVX/
        VVVV/1VVVf9VVVX9VVVVmVVVVQkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABVVVUwU1NTllVVVdlU
        VFT5VFRU+VVVVdlTU1OWVVVVMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAACAAAABAAAAAAQAg
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAABJSUkOU1NTWVRUVJtUVFTLVFRU7FRUVPxUVFT8VFRU7FRUVMtUVFSbU1NTWUlJSQ4A
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAABTU1MlVVVVnFRUVPVVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VFRU9VVVVZxTU1MlAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAABVVVUJVFRUjFVVVfpVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVfpUVFSMVVVVCQAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVVVVJFVVVdNVVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVXT
        VVVVJAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFNTUzFVVVXqVVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf9VVVXqU1NTMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABVVVUkVVVV
        6lVVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVXqVVVVJAAAAAAAAAAAAAAAAAAAAAAA
        AAAAVVVVCVVVVdNVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVXTVVVV
        CQAAAAAAAAAAAAAAAAAAAABUVFSMVVVV/1VVVf+pqan/w8PD/2lpaf9VVVX/VVVV/1VVVf9VVVX/
        VVVV/6ysrP/ExMT/b29v/1VVVf9VVVX/VVVV/1VVVf+ampr/4+Pj/9nZ2f9YWFj/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9UVFSMAAAAAAAAAAAAAAAAU1NTJVVVVfpVVVX/VVVV/9TU1P//////enp6/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/1dXV//////+EhIT/VVVV/1VVVf9VVVX/VlZW//Hx8f//////////
        /3d3d/9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVfpTU1MlAAAAAAAAAABVVVWcVVVV/1VVVf9VVVX/
        1NTU//////94eHj/VVVV/1VVVf9VVVX/VVVV/1VVVf/T09P//////4SEhP9VVVX/VVVV/1VVVf9z
        c3P//////+np6f//////nJyc/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVZwAAAAASUlJDlRU
        VPVVVVX/VVVV/1VVVf/U1NT//////3d3d/9VVVX/VVVV/1VVVf9VVVX/VVVV/9HR0f//////hISE
        /1VVVf9VVVX/VVVV/5qamv//////urq6///////BwcH/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        VFRU9UlJSQ5TU1NZVVVV/1VVVf9VVVX/VVVV/9TU1P//////dnZ2/1VVVf+ZmZn/0dHR/1VVVf9V
        VVX/z8/P//////+EhIT/VVVV/1VVVf9VVVX/wcHB//////+RkZH/9fX1/+bm5v9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/U1NTWVRUVJtVVVX/VVVV/1VVVf9VVVX/1NTU//////90dHT/VVVV
        /9jY2P//////dnZ2/1VVVf/Nzc3//////4SEhP9VVVX/VVVV/1VVVf/n5+f//////3V1df/d3d3/
        /v7+/2JiYv9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9UVFSbVFRUy1VVVf9VVVX/VVVV/1VVVf/U
        1NT//////3Nzc/9mZmb//v7+//////+wsLD/VVVV/8rKyv//////hISE/1VVVf9VVVX/ZGRk//7+
        /v/9/f3/Wlpa/8PDw///////h4eH/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1RUVMtUVFTsVVVV
        /1VVVf9VVVX/VVVV/9TU1P//////bm5u/5ycnP//////8fHx/+rq6v9VVVX/xMTE//////+EhIT/
        VVVV/1VVVf+Kior//////+Tk5P9VVVX/pqam//////+srKz/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VFRU7FRUVPxVVVX/VVVV/1VVVf9VVVX/1NTU//////9nZ2f/0tLS//r6+v+jo6P//////3p6
        ev+7u7v//////4SEhP9VVVX/VVVV/6+vr///////wsLC/1VVVf+Hh4f//////9HR0f9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9UVFT8VFRU/FVVVf9VVVX/VVVV/1VVVf/U1NT//////2dnZ//7+/v/
        0NDQ/25ubv//////rq6u/7Gxsf//////hISE/1VVVf9VVVX/1dXV//////+dnZ3/VVVV/2RkZP/+
        /v7/9fX1/1ZWVv9VVVX/VVVV/1VVVf9VVVX/VVVV/1RUVPxUVFTsVVVV/1VVVf9VVVX/VVVV/9TU
        1P/7+/v/i4uL//////+ampr/VVVV/+fn5//e3t7/paWl//////+EhIT/VVVV/1dXV//39/f/////
        /3h4eP9VVVX/VVVV/+vr6///////cnJy/1VVVf9VVVX/VVVV/1VVVf9VVVX/VFRU7FRUVMtVVVX/
        VVVV/1VVVf9VVVX/1NTU//Dw8P+6urr//v7+/2ZmZv9VVVX/s7Oz//7+/v+oqKj//////4SEhP9V
        VVX/dXV1///////5+fn/WVlZ/1VVVf9VVVX/yMjI//////+Xl5f/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9UVFTLVFRUm1VVVf9VVVX/VVVV/1VVVf/U1NT/4+Pj/+rq6v/Z2dn/VVVV/1VVVf9/f3//////
        /8rKyv//////hISE/1VVVf+ampr//////9nZ2f9VVVX/VVVV/1VVVf+lpaX//////7y8vP9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1RUVJtTU1NZVVVV/1VVVf9VVVX/VVVV/9TU1P/v7+///////6SkpP9V
        VVX/VVVV/1dXV//z8/P/7e3t//////+EhIT/VVVV/8DAwP//////tLS0/1VVVf9VVVX/VVVV/4KC
        gv//////4uLi/1VVVf9VVVX/VVVV/1VVVf9VVVX/U1NTWUlJSQ5UVFT1VVVV/1VVVf9VVVX/1NTU
        ////////////bm5u/1VVVf9VVVX/VVVV/8HBwf///////////4SEhP9VVVX/5ubm//////+Pj4//
        VVVV/1VVVf9VVVX/YGBg//7+/v/9/f3/Xl5e/1VVVf9VVVX/VVVV/1RUVPVJSUkOAAAAAFVVVZxV
        VVX/VVVV/1VVVf/U1NT//////+Pj4/9VVVX/VVVV/1VVVf9VVVX/jo6O////////////hISE/2Fh
        Yf/+/v7//////2pqav9VVVX/VVVV/1VVVf9VVVX/5ubm//////+CgoL/VVVV/1VVVf9VVVX/VVVV
        nAAAAAAAAAAAU1NTJVVVVfpVVVX/VVVV/9TU1P//////ra2t/1VVVf9VVVX/VVVV/1VVVf9eXl7/
        +/v7//////+EhIT/hYWF///////v7+//VVVV/1VVVf9VVVX/VVVV/1VVVf/Dw8P//////6enp/9V
        VVX/VVVV/1VVVfpTU1MlAAAAAAAAAAAAAAAAVFRUjFVVVf9VVVX/ubm5/+Hh4f91dXX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf+8vLz/4eHh/3x8fP+Tk5P/4eHh/7m5uf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /4+Pj//h4eH/tbW1/1VVVf9VVVX/VFRUjAAAAAAAAAAAAAAAAAAAAABVVVUJVVVV01VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVdNVVVUJAAAAAAAAAAAAAAAAAAAAAAAA
        AABVVVUkVVVV6lVVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVXqVVVVJAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAABTU1MxVVVV6lVVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV6lNT
        UzEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABVVVUkVVVV01VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        VVVV/1VVVdNVVVUkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABV
        VVUJVFRUjFVVVfpVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVfpUVFSMVVVVCQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAU1NTJVVVVZxUVFT1VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1RUVPVVVVWcU1NTJQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAElJSQ5TU1NZVFRUm1RU
        VMtUVFTsVFRU/FRUVPxUVFTsVFRUy1RUVJtTU1NZSUlJDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAADAAAABgAAAA
        AQAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFVVVUSU1NTJVJSUktTU1OHVFRUtlVV
        VdhUVFTwVFRU/FRUVPxUVFTwVFRU2lNTU7hTU1OHUlJSTlFRUSZVVVUSAAAAAgAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAQEAEUFBQMFVVVXJU
        VFSxVVVV5FRUVP5VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VFRU/lRU
        VOZUVFSxVVVVdVBQUDNAQEAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAE5OThpUVFSkVVVV6FVVVfpVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VFRU+1VVVepUVFSkTU1NIQAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAABRUVEWVFRUc1VVVfFVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VFRU8lRUVHlRUVEWAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFRUVDpUVFS3VVVV+VVVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1RUVPtUVFS3VFRUQAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABUlJSZlVV
        VexUVFT+VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9UVFT+
        VVVV7VNTU24AAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAACoqKgZTU1NyVFRU8lVVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVfZTU1NyQEBACAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVRUVGpUVFTtVVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9UVFTtU1NT
        cgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUlJSZlVVVfZVVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/VVVV9lNTU24AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAABUVFRAVVVV5VVVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVe1UVFRAAAAAAQAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAERERA9UVFS3VVVV/VVVVf9cXFz/bm5u/29vb/9jY2P/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9cXFz/bm5u/29vb/9lZWX/VlZW/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1hYWP+BgYH/jo6O/4iIiP9paWn/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1RUVP5UVFS3UVFRFgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFVVVW9UVFT7VVVV/1VV
        Vf97e3v/4uLi//Dw8P/Dw8P/YWFh/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9+fn7/4+Pj
        //Dw8P/Ly8v/ZGRk/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/42Njf/09PT/+Pj4//b29v+pqan/
        V1dX/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9UVFT7VFRUeQAAAAAAAAAAAAAAAAAAAAAA
        AAAAVVVVHlVVVfFVVVX/VVVV/1VVVf9/f3//7+/v///////Pz8//Y2Nj/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf+AgID/7+/v///////Z2dn/ZmZm/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /9zc3P/////////////////Gxsb/X19f/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        VFRU8k1NTSEAAAAAAAAAAAAAAABAQEAEU1NTmVVVVf9VVVX/VVVV/1VVVf9/f3//7+/v///////O
        zs7/YmJi/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9/f3//7+/v///////Z2dn/ZmZm/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/aGho//z8/P//////9vb2///////e3t7/aGho/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1RUVKRAQEAEAAAAAAAAAABQUFAzVFRU4VVVVf9VVVX/
        VVVV/1VVVf9/f3//7+/v///////Nzc3/YmJi/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9+
        fn7/7u7u///////Z2dn/ZmZm/1VVVf9VVVX/VVVV/1VVVf9VVVX/kpKS////////////zs7O////
        ///39/f/cnJy/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVepQUFAzAAAA
        AAAAAAFVVVV1VVVV+VVVVf9VVVX/VVVV/1VVVf9/f3//7+/v///////MzMz/YWFh/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf98fHz/7u7u///////Z2dn/ZmZm/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/vLy8///////+/v7/nJyc////////////kpKS/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1RUVPtVVVV1AAAAAlVVVQxUVFSxVVVV/1VVVf9VVVX/VVVV/1VVVf9/f3//7+/v
        ///////Ly8v/YWFh/1VVVf9VVVX/enp6/4uLi/9kZGT/VVVV/1VVVf97e3v/7e3t///////Z2dn/
        ZmZm/1VVVf9VVVX/VVVV/1VVVf9bW1v/3Nzc///////z8/P/eHh4//v7+///////ubm5/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9UVFSxVVVVElJSUhlUVFTmVVVV/1VV
        Vf9VVVX/VVVV/1VVVf9/f3//7+/v///////Kysr/YWFh/1VVVf9bW1v/19fX//X19f+ampr/VVVV
        /1VVVf95eXn/7Ozs///////Z2dn/ZmZm/1VVVf9VVVX/VVVV/1VVVf9zc3P/6urq///////g4OD/
        aWlp/+bm5v//////4uLi/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9U
        VFTmUVFRJlRUVEBUVFT+VVVV/1VVVf9VVVX/VVVV/1VVVf9/f3//7+/v///////Jycn/YGBg/1VV
        Vf97e3v/7e3t///////CwsL/Xl5e/1VVVf94eHj/7Ozs///////Z2dn/ZmZm/1VVVf9VVVX/VVVV
        /1VVVf+MjIz/9PT0///////Ozs7/YmJi/8rKyv///////f39/2JiYv9VVVX/VVVV/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9UVFT+UlJSTlNTU35VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9/
        f3//7+/v///////Jycn/YGBg/1VVVf+fn5//+vr6///////o6Oj/bGxs/1VVVf93d3f/6+vr////
        ///Z2dn/ZmZm/1VVVf9VVVX/VVVV/1VVVf+lpaX//Pz8//////+8vLz/W1tb/66urv//////////
        /4yMjP9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/U1NTh1VVVbJVVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9/f3//7+/v///////Hx8f/YGBg/1tbW//FxcX//v7+///////9
        /f3/kpKS/1VVVf90dHT/6+vr///////Z2dn/ZmZm/1VVVf9VVVX/VVVV/1paWv/AwMD//v7+//7+
        /v+oqKj/VVVV/46Ojv///////////7m5uf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/U1NTuFRUVNdVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9/f3//7+/v///////ExMT/
        Xl5e/2VlZf/o6Oj///////X19f//////z8/P/1VVVf9wcHD/6enp///////Z2dn/ZmZm/1VVVf9V
        VVX/VVVV/2BgYP/Z2dn///////n5+f+UlJT/VVVV/3BwcP/8/Pz//////+Dg4P9XV1f/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VFRU2lRUVO9VVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf9/f3//7+/v///////AwMD/XV1d/4SEhP/9/f3//////6qqqv/9/f3/+fn5/2pqav9ra2v/
        5+fn///////Z2dn/ZmZm/1VVVf9VVVX/VVVV/2dnZ//x8fH///////T09P9/f3//VVVV/2VlZf/s
        7Oz//////+/v7/9qamr/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VFRU8FRU
        VPxVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9/f3//7+/v//////+6urr/W1tb/8LCwv//////8fHx
        /2hoaP/o6Oj//////6mpqf9lZWX/5eXl///////Z2dn/ZmZm/1VVVf9VVVX/VVVV/4GBgf/+/v7/
        /////+7u7v9mZmb/VVVV/19fX//V1dX///////X19f+Dg4P/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VFRU/FRUVPtVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9/f3//7+/v////
        //+0tLT/X19f//X19f//////wMDA/11dXf/Kysr//////97e3v9hYWH/4uLi///////Z2dn/ZmZm
        /1VVVf9VVVX/VVVV/6urq////////////93d3f9VVVX/VVVV/1paWv++vr7//v7+//v7+/+bm5v/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VFRU/FRUVO9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9/f3//7+/v//7+/v+srKz/h4eH///////8/Pz/ioqK/1ZWVv+rq6v//f39//Dw
        8P9zc3P/3t7e///////Z2dn/ZmZm/1VVVf9VVVX/VVVV/9bW1v///////////7Ozs/9VVVX/VVVV
        /1VVVf+np6f//Pz8//7+/v+0tLT/WVlZ/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        VFRU8FVVVdVVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9/f3//7+/v//39/f+lpaX/vLy8///////l
        5eX/a2tr/1VVVf+IiIj/8vLy//n5+f+SkpL/1NTU///////Z2dn/ZmZm/1VVVf9VVVX/XFxc//r6
        +v///////////4eHh/9VVVX/VVVV/1VVVf+Pj4//9fX1///////Ozs7/YmJi/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV2FRUVLBVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9/f3//
        7+/v//v7+/+np6f/4ODg//7+/v/CwsL/Xl5e/1VVVf9nZ2f/5OTk//7+/v+wsLD/y8vL///////Z
        2dn/ZmZm/1VVVf9VVVX/gICA////////////+/v7/2BgYP9VVVX/VVVV/1VVVf94eHj/7Ozs////
        ///m5ub/a2tr/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VFRUtlNTU35VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9/f3//7+/v//n5+f+9vb3/7u7u//v7+/+fn5//VVVV/1VVVf9VVVX/
        w8PD///////Pz8//yMjI///////Z2dn/ZmZm/1VVVf9VVVX/qKio////////////39/f/1VVVf9V
        VVX/VVVV/1VVVf9iYmL/4+Pj///////6+vr/enp6/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/U1NTh1RUVD1UVFT+VVVV/1VVVf9VVVX/VVVV/1VVVf9/f3//7+/v//f39//U1NT/+vr6
        //Pz8/96enr/VVVV/1VVVf9VVVX/ioqK///////v7+//xsbG///////Z2dn/ZmZm/1VVVf9VVVX/
        0dHR////////////tra2/1VVVf9VVVX/VVVV/1VVVf9VVVX/y8vL////////////np6e/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9UVFT+UlJSS1JSUhlVVVXkVVVV/1VVVf9VVVX/VVVV/1VV
        Vf9/f3//7+/v//n5+f/q6ur//////+Pj4/9bW1v/VVVV/1VVVf9VVVX/XFxc//X19f//////2dnZ
        ///////Z2dn/ZmZm/1VVVf9lZWX/5eXl///////+/v7/j4+P/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        p6en////////////xsbG/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9UVFTkU1NTJVVVVQxU
        VFSxVVVV/1VVVf9VVVX/VVVV/1VVVf9/f3//7+/v//7+/v/7+/v//////7CwsP9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/8HBwf//////9/f3///////Z2dn/ZmZm/1VVVf9+fn7/7u7u///////19fX/c3Nz
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/goKC////////////7Ozs/1ZWVv9VVVX/VVVV/1VVVf9VVVX/
        VVVV/1VVVf9UVFSxVVVVEgAAAABVVVVyVFRU+FVVVf9VVVX/VVVV/1VVVf9/f3//7+/v////////
        /////////29vb/9VVVX/VVVV/1VVVf9VVVX/VVVV/4ODg//+/v7////////////Z2dn/ZmZm/1VV
        Vf+YmJj/+Pj4///////d3d3/aGho/1VVVf9VVVX/VVVV/1VVVf9VVVX/XV1d//z8/P///////v7+
        /3BwcP9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVfpVVVVyAAAAAQAAAABQUFAwVVVV31VVVf9VVVX/
        VVVV/1VVVf9/f3//7+/v////////////39/f/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/2VlZf/r
        6+v////////////Z2dn/ZmZm/1ZWVv+wsLD//v7+///////FxcX/X19f/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/93d3f///////////5qamv9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVehQUFAwAAAA
        AAAAAABAQEAEU1NTmVVVVf9VVVX/VVVV/1VVVf9/f3//7+/v////////////pqam/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1xcXP/Jycn////////////Z2dn/ZmZm/1xcXP/IyMj///////7+/v+t
        ra3/V1dX/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/7W1tf///////////8XFxf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1RUVKRAQEAEAAAAAAAAAAAAAAAAVVVVGFRUVPBVVVX/VVVV/1VVVf9/f3//7+/v
        ///////19fX/dHR0/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf+lpaX//Pz8///////Z2dn/
        ZmZm/2JiYv/h4eH///////n5+f+Tk5P/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/4qKiv//
        /////////+jo6P9bW1v/VVVV/1VVVf9VVVX/VVVV8U5OThoAAAAAAAAAAAAAAAAAAAAAAAAAAFVV
        VWlVVVX5VVVV/1VVVf96enr/5OTk//Pz8//Ozs7/ZGRk/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf+BgYH/5ubm//Pz8//Q0ND/ZWVl/2ZmZv/r6+v/8/Pz/+np6f96enr/VVVV/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/2lpaf/s7Oz/8/Pz/+bm5v9vb2//VVVV/1VVVf9VVVX5VFRUcwAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAERERA9UVFS3VVVV/VVVVf9eXl7/hYWF/4yMjP95eXn/WFhY/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9cXFz/hISE/4yMjP+AgID/Wlpa/1tbW/+JiYn/jIyM
        /4eHh/9dXV3/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1lZWf+BgYH/jIyM/4iIiP9iYmL/
        VVVV/1RUVP5UVFS3UVFRFgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABUVFQ6VVVV41VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVexUVFQ6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAU1NTX1VVVfFVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VFRU8lJSUmYAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVRUVGpUVFTtVVVV/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9UVFTtU1NTcgAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AEBAQARUVFRqVVVV8VVVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVfZUVFRqKioqBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABU1NTX1VVVeNVVVX9VVVV/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/
        VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX9VVVV5VJSUmYAAAABAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFRU
        VDpUVFS3VVVV+VVVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1RUVPtUVFS3
        VFRUQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEREQPVVVVaVRUVPBVVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV
        /1VVVf9VVVX/VVVV8VVVVW9EREQPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFVVVRhT
        U1OZVVVV31RUVPhVVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VVVV/1VV
        Vf9VVVX/VVVV/1VVVf9VVVX/VVVV+VRUVOFTU1OZVVVVHgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAABAQEAEUFBQMFVVVXJUVFSxVVVV5FRUVP5VVVX/VVVV/1VVVf9V
        VVX/VVVV/1VVVf9VVVX/VVVV/1VVVf9VVVX/VFRU/lRUVOZUVFSxVVVVdVBQUDNAQEAEAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABVVVUM
        UlJSGVRUVD1TU1N+VFRUsFVVVdVUVFTvVFRU+1RUVPxUVFTvVFRU11VVVbJTU1N+VFRUQFJSUhlV
        VVUMAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAA=="""
    return base64.b64decode(icon)
