# Python_YoutubeDownloader
- A Youtube Videos downloader made with pytube module.
- Not restricted videos are downloaded only.
- Only Progressive Downloads are possible.
- Max Quality present 720p.

### Screen Shots
- Main Window
![2020-08-29 (11)](https://user-images.githubusercontent.com/64532019/91641633-56e86280-ea43-11ea-9305-e83c1d7d98ec.png)



### Enter the url in the url tab, select the Video Quality, Hit Download 😁😁😁.



## Due to some changes in the youtube policy and in the pytube module the pytube V-9.6.0 is no longer working

### ERROR:
- site-packages\pytube\extract.py", line 143, in js_url base_js = get_ytplayer_config(html)["assets"]["js"] KeyError: 'assets'

### FIX:
- Uninstall current version of pytube by using command:  pip uninstall pytube
- Install new version of pytube i.e. V-9.7.0 by using command:  pip install git+https://github.com/nficano/pytube 
- The above command will clone the repository of new pytube module and will install it on the device since the new module of pytube has not been released yet.
- No changes in the basic usage of pytube module, usage as according to the original pytube documentation.
- Full discussion on the issue: https://github.com/nficano/pytube/issues/777

