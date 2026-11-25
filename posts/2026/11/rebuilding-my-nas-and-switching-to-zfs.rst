I am finally done with the last hardware refresh on my rack. My NAS is now running recent hardware. I have all of my servers on similar hardware now (NVME, Intel Core Ultra, DDR5). This is easier to have everything on the same hardware, especially since I build my own kernels.

As part of this process, I also decided to upgrade my disks. I have running a RAID-6 on 13 3TB hard drives. These were great disks when I started, but not so great today. The olest disk in the RAID was 13 years old. Therefore, it also made sense to upgrade the disks since they could be failing. So I switched to fewer Seagate Exos disks instead.

This is not the best year to purchase new hardware. I could have waited, but I am not sure that next year or the year after is going to be even better. So I decided to upgrade them regardless. 

Finally, I switched from an mdadm RAD-6 with LVM volumes to ZFS. I am using RAIDZ-2 for my disks to get some strong redundancy. I did have some little ZFS experience from FreeBSD, but really not much. Overall, it was a breeze to set up. And it is really great that we can set up pools and datasets so easily. It is much better than what I was doing before with LVM. The main issue with LVM volumes was growing them. Now, I will not have this problem anymore.

Overall, I am happy with how it turned out. The foundation on my rack should be good for many years again.

What about you? Have you tried ZFS?
