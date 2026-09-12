# -*- coding: utf-8 -*-
"""
Assembler per Modulo 2: Gli Anni Sessanta
Capitoli da C18 a C40 (23 capitoli completi)
"""
import mod2_part1
import build_mod2_sub1
import build_mod2_sub2
import build_mod2_sub3
import build_mod2_sub4

def get_mod2_chapters():
    chaps = []
    chaps.extend(mod2_part1.chaps)
    chaps.extend(build_mod2_sub1.get_sub1_chapters())
    chaps.extend(build_mod2_sub2.get_sub2_chapters())
    chaps.extend(build_mod2_sub3.get_sub3_chapters())
    chaps.extend(build_mod2_sub4.get_sub4_chapters())
    return chaps

if __name__ == '__main__':
    c = get_mod2_chapters()
    print("Module 2 assembled successfully:", len(c), "chapters.")
    for x in c:
        print(f"  {x['id']} (#{x['number']}): {x['title']}")
