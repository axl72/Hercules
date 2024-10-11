import os, uuid, tempfile as tf


def make_temp_name(dir=tf.gettempdir()) -> str:
    return os.path.join(dir, str(uuid.uuid1()))
