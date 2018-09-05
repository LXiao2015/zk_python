import zkclient
from zkclient import ZKClient

zk = ZKClient("10.187.176.194:2181")

newKeyList = [
    "goods_homef~~~brand",
    "qrqm_hp_cfb~~~brand",
    "goods_homef~~~c3brand",
    "qrqm_hp_cfb~~~c3brand_0",
    "goods_homef~~~c3",
    "qrqm_hp_cfb~~~c3",
    "qrqm_hp_cfb~~~channelBrand_0",
    "qrqm_hp_cfb~~~channelC3Brand_0",
    "qrqm_hp_cfb~~~channelC3_0",
    "qrqm_hp_cfb~~~channel",
    "cd3_fzxp_fs",
    "cd3_jdjx_fs",
    "cd3_jdmarket_fs",
    "cd3_newsh_fs",
    "cd3_oversea_fs",
    "cd3_7toreturn_fs",
    "seckill_cfb~~~brand_code",
    "seckill_cfb~~~cid3_discount_ratio_cat",
    "seckill_cfb~~~cid3",
    "seckill_cfb~~~cid3_pw3_ids",
    "seckill_cfb~~~discount_amount_cat",
    "seckill_cfb~~~discount_ratio_cat"
]

created = zk.exists("/root/redis");

if created:
    print 'deleting /root/redis ...'
    oldKeyList = zk.get_children("/root/redis");
    for k in oldKeyList:
        zk.delete("/root/redis/" + k);
else:
    zk.create("/root/redis", "");
for k in newKeyList:
    zk.create("/root/redis/" + k, k);

print 'add keys on zk success!'
