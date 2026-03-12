# Mod 26
- ROT13
```
echo "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}" > value.txt
cat value.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
Output and answer: `picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}`

With Python:
py```
>>> import codecs
>>> print(codecs.decode("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}", 'rot_13'))
picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}
>>> 
```