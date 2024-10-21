import cv2 as cv


def Frameresize(frame,scale=0.50):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)

    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)


capture=cv.VideoCapture('Video/testing.mp4')
while True:
    isTrue, frames=capture.read()

    if not isTrue:
        print("End of video or failed to read frame.")
        break
    frame_resize=Frameresize(frames)
    cv.imshow('Video',frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()