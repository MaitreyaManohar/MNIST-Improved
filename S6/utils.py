import matplotlib.pyplot as plt


def viewPlots(batch_data,batch_label,n_images):
    fig = plt.figure()  
    for i in range(n_images):
        plt.subplot(int(n_images/2),2,i+1)
        plt.tight_layout()
        plt.imshow(batch_data[i].squeeze(0), cmap='gray')
        print('batch_data[i]: ', batch_data[i].shape)
        plt.title(batch_label[i].item())
        plt.xticks([])
        plt.yticks([])