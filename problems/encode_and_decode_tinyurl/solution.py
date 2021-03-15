class Codec:
    
    def __init__(self):
        self.urls = []
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
       #map[] = "abcdefghijklmnopqrstuvwxyzABCDEF"
        #         "GHIJKLMNOPQRSTUVWXYZ0123456789";
        
        #target = "".join(longUrl.split("/")[3:])
        self.urls.append(longUrl)
        
        #Convert given integer id to a base 62 number
        #while n :
         #   shorturl.push_back(map[n%62])
          #  n = n/62
        
  
        # Reverse shortURL to complete base conversion
        #reverse(shorturl.begin(), shorturl.end())
        url = "http://tinyurl.com/%d" % (len(self.urls))
        print(url)
        return url


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        target = "".join(shortUrl.split("/")[3:])
        url = self.urls[int(target)-1]
        return url

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))