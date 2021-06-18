import tensorflow as tf
# 상수 노드
node = tf.constant(100)

# session
sess = tf.Session()

# 실행
print(sess.run(node))