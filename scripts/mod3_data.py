# -*- coding: utf-8 -*-
"""
Assembler per Modulo 3: Gli Anni Settanta
Capitoli da C41 a C53 (13 capitoli completi)
"""
import build_mod3_sub1
import build_mod3_sub2

def get_mod3_chapters():
    chaps = []
    chaps.extend(build_mod3_sub1.get_sub1_chapters())
    chaps.extend(build_mod3_sub2.get_sub2_chapters())
    return chaps

if __name__ == '__main__':
    c = get_mod3_chapters()
    print("Module 3 assembled successfully:", len(c), "chapters.")
    for x in c:
        print(f"  {x['id']} (#{x['number']}): {x['title']}")
