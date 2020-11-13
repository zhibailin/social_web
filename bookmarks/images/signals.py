from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


# 通过 receiver 装饰器 将 `users_like_changed` 注册为 receiver function 并为其附加 `m2m_change` signal
# receiver 连接 sender -- Image.users_like.through，
# 只有 signal 被 sender 发送时，receiver function 才会执行
@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()
