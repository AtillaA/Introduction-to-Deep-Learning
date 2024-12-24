import numpy as np


def affine_forward(x, w, b):
    """
    Computes the forward pass for an affine (fully-connected) layer.

    The input x has shape (N, d_1, ..., d_k) and contains a minibatch of N
    examples, where each example x[i] has shape (d_1, ..., d_k). We will
    reshape each input into a vector of dimension D = d_1 * ... * d_k, and
    then transform it to an output vector of dimension M.

    Inputs:
    :param x: A numpy array containing input data, of shape (N, d_1, ..., d_k)
    :param w: A numpy array of weights, of shape (D, M)
    :param b: A numpy array of biases, of shape (M,)

    :return out: output, of shape (N, M)
    :return cache: (x, w, b)
    """
    out = None
    x_reshaped = np.reshape(x, (x.shape[0], -1))
    out = x_reshaped.dot(w) + b
    cache = (x, w, b)
    return out, cache


def affine_backward(dout, cache):
    """
    Computes the backward pass for an affine layer.

    Inputs:
    :param dout: Upstream derivative, of shape (N, M)
    :param cache: Tuple of:
      - x: Input data, of shape (N, d_1, ... d_k)
      - w: Weights, of shape (D, M)
      - b: A numpy array of biases, of shape (M,

    :return dx: Gradient with respect to x, of shape (N, d1, ..., d_k)
    :return dw: Gradient with respect to w, of shape (D, M)
    :return db: Gradient with respect to b, of shape (M,)
    """
    x, w, b = cache
    dx, dw, db = None, None, None
    dw = np.reshape(x, (x.shape[0], -1)).T.dot(dout)
    dw = np.reshape(dw, w.shape)

    db = np.sum(dout, axis=0, keepdims=False)

    dx = dout.dot(w.T)
    dx = np.reshape(dx, x.shape)
    return dx, dw, db


class Sigmoid:
    def __init__(self):
        pass

    def forward(self, x):
        """
        :param x: Inputs, of any shape

        :return out: Output, of the same shape as x
        :return cache: Cache, for backward computation, of the same shape as x
        """
        outputs = 1 / (1 + np.exp(-x))
        cache = outputs
        return outputs, cache

    def backward(self, dout, cache):
        """
        :return: dx: the gradient w.r.t. input X, of the same shape as X
        """
        dx = None
        dx = dout * cache * (1 - cache)
        return dx


class Relu:
    def __init__(self):
        pass

    def forward(self, x):
        """
        :param x: Inputs, of any shape

        :return out: Output, of the same shape as x
        :return cache: Cache, for backward computation, of the same shape as x
        """
        outputs = None
        cache = None
        ########################################################################
        # TODO:                                                                #
        # Implement the forward pass of Relu activation function               #
        ########################################################################

        outputs = np.maximum(x, 0)
        cache = x

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return outputs, cache

    def backward(self, dout, cache):
        """
        :return: dx: the gradient w.r.t. input X, of the same shape as X
        """
        dx = None
        ########################################################################
        # TODO:                                                                #
        # Implement the backward pass of Relu activation function              #
        ########################################################################

        x = cache
        dx = dout
        dx[x < 0] = 0

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return dx


class LeakyRelu:
    def __init__(self, slope=0.01):
        self.slope = slope

    def forward(self, x):
        """
        :param x: Inputs, of any shape

        :return out: Output, of the same shape as x
        :return cache: Cache, for backward computation, of the same shape as x
        """
        outputs = np.zeros(x.shape)
        cache = np.zeros(x.shape)
        ########################################################################
        # TODO:                                                                #
        # Implement the forward pass of LeakyRelu activation function          #
        ########################################################################

        # ReLU difference: when input <= 0, output is not 0 but (x * slope) which is .01 by default
        cache = np.copy(x)
        outputs = np.copy(x)
        outputs[x <= 0] *= self.slope

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return outputs, cache

    def backward(self, dout, cache):
        """
        :return: dx: the gradient w.r.t. input X, of the same shape as X
        """
        dx = np.zeros((cache*dout).shape)
        ########################################################################
        # TODO:                                                                #
        # Implement the backward pass of LeakyRelu activation function         #
        ########################################################################

        # ReLU difference: when cache <= 0, gradient is not 0 but the slope
        x = cache
        d = np.ones_like(x)
        d[x <= 0] = self.slope
        dx = d * dout

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return dx


class Tanh:
    def __init__(self):
        pass

    def forward(self, x):
        """
        :param x: Inputs, of any shape

        :return out: Output, of the same shape as x
        :return cache: Cache, for backward computation, of the same shape as x
        """
        outputs = np.ones(x.shape)
        cache = np.ones(x.shape)
        ########################################################################
        # TODO:                                                                #
        # Implement the forward pass of Tanh activation function               #
        ########################################################################

        outputs = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
        cache = outputs

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return outputs, cache

    def backward(self, dout, cache):
        """
        :return: dx: the gradient w.r.t. input X, of the same shape as X
        """
        dx = np.ones((cache*dout).shape)
        ########################################################################
        # TODO:                                                                #
        # Implement the backward pass of Tanh activation function              #
        ########################################################################

        # backward pass is: dy/dx = [ 4 / (e^x + e^(-x))^2 ]
        #                         = [ 1 - ((e^x - e^(-x)) / (e^x + e^(-x)))^2
        x = cache
        dx = 1 - x ** 2
        dx = dx * dout

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return dx