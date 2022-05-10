# IBM X-Force analysis

## Just run 

``` 
pip install -r requirements.txt

```
## Then run this to scan multiple IPs with X-Force by IBM on new tabs on the chromedriver

```
python IBMSearch.py -l list.txt
```

You can also take screenshots of a single IP address analysis. Just type:
```
python IBMSearch.py --ip X.X.X.X
```
This works well on windows. If you want to use it on linux you will need to change the line 62 command what is the program what loads images on your system (for example, shotwell, gthumb, gnwview, eom, kphotoalbum, etc.)

This is licensed by the GNU GPL3 license.
