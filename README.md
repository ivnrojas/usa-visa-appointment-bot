# usa-visa-appointment-bot

Apparently I need to replicate the entire request. All the headers must be the same
than the one we run in the browser. 
And after we send a request we get a Set-Cookie instruction. That cookie value is the one that we need.

So the first time we call it, it will give us an empty response because we don't have
all exact data of the cookie. But that call will give us the information of the next
cookie we need to send. Such as:

_yatri_session=bFphVE9vREVqRGVRUjRiMXFrVm5BOHBNb01TMHhCTTVUR0g2cThzRW9VTHR0T3FHWHk4eXFJc2ZRT3E1VEJNeFNSeE9GUXdKRSt1bXh3bnAvRmkzN00rYkZTR05WSm9pMUxMUHdLN2NtR09qZ2RxVXU2UXpiQk85ZDJrRmtXQ0sxNWY3UjFpQUVVZlhCSUR5aVl4WHMvcEc0c2dXMmFySXVua1owNnFTb0pwM1VuZnRaY0E5MWYwV3dORmgxeEsyK1hKc29nS1BZSXdOS0R0S2ZnaTZIcEFmSkxsVHNwcTFUSTBWSzRDWUJVNXl0c0tYa21xS2U5RnZ1Njk0c1pzZm4xL3dOWERSTVhhS01DaWU3YzllaFMzN2N2NXJxdCtVNWxnc0lmMFRQbDlGRDdMRUhsRDgwVEhDcXFmWjlnaWFBSStMWnVpejJlZEEyTzIxbEtwNWhnek9YcS9TM1hGeW5mMENjV0NMK2xpZlVtSkZ1Mk1YSm90ZVJTOFl0RGx4RzF4Nm9LVTJrdW1aMXVyVy9jRVVTYmJJa3ppOWtOOHVyU0pFNVZITFBnNjFaSytGTjlQQmJjdlRzaVh1WXlDS2pER2VFSzdJemxJam5EUXUyTGU3dlBhRnRqSldTZFFuaXd5RURBS2VSYXZDSG10UllLMTBkZ2srMkRLRzF6cldZbnR1Ym1NOFNjbjVvajZCdGhrMzJFeTM3SlhwTSswckc5T3FzNFRRV2hnPS0tNmx1ZEJpWGhUNDF3bTU5dXRyR285dz09--c7bde2965aea92d833c1faeb64504ce5a42bc3e7; path=/; HttpOnly; Secure; SameSite=None

So that's the one we need to do all this shit. Just set that value for the yatri session cookie and the rest it's done.