#!/usr/bin/env python3
"""
trains a loaded neural network model using mini-batch gradient descent
"""
import tensorflow as tf
shuffle_data = __import__('2-shuffle_data').shuffle_data


def train_mini_batch(x_train, y_train, x_valid, y_valid,
                     batch_size=32, epochs=5,
                     load_path="/tmp/model.ckpt",
                     save_path="/tmp/model.ckpt"):
    """
    trains a loaded neural network model using mini-batch
    gradient descent
    """
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph(load_path + '.meta')
        saver.restore(sess, load_path)

        x = tf.get_collection("x")[0]
        y = tf.get_collection("y")[0]
        accuracy = tf.get_collection("accuracy")[0]
        loss = tf.get_collection("loss")[0]
        train_op = tf.get_collection("trian_op")[0]

        m = x_train.shape[0]
        if x_train.shape[0] % batch_size != 0:
            size += 1

        for epoch in range(epochs + 1):
            train_cost = sess.run(loss, feed_dict={x: x_train, y: y_train})
            train_acc = sess.run(accuracy, feed_dict={x: x_train, y: y_train})
            valid_cost = sess.run(loss, feed_dict={x: x_valid, y: y_valid})
            valid_acc = sess.run(accuracy, feed_dict={x: x_valid, y: y_valid})
            print("After {} epochs:".format(epoch))
            print("\tTraining Cost: {}".format(train_cost))
            print("\tTraining Accuracy: {}".format(train_acc))
            print("\tValidation Cost: {}".format(valid_cost))
            print("\tValidation Accuracy: {}".format(valid_acc))

            if epoch < epochs:
                X_shuffled, Y_shuffled = shuffle_data(x_train, y_train)
                for step in range(size):
                    start = step * batch_size
                    end = start + batch_size
                    sess.run(train_op,
                             feed_dict={x: X_shuffled[start:end],
                                        y: Y_shuffled[start:end]})

                    if (step + 1) % 100 == 0 and step > 0:
                        step_cost = sess.run(loss,
                                             feed_dict=
                                             {x: X_shuffled[start:end],
                                              y: Y_shuffled[start:end]})
                        step_acc = sess.run(accuracy,
                                            feed_dict={
                                                x: X_shuffled[start:end],
                                                y: Y_shuffled[start:end]})
                        print("\tStep {}:".format(step + 1))
                        print("\t\tCost: {}".format(step_cost))
                        print("\t\tAccuracy: {}".format(step_acc))

        return saver.save(sess, save_path)
        