import bentoml, streamlit
from pathlib import Path
import typing as t
from bentoml.validators import ContentType
import tempfile
import os
<<<<<<< Updated upstream

src_image, dst_image = streamlit.columns(2)
result = None
bentoml_host = os.getenv("BENTOML_SERVICE", "http://backend:3000")

Image = t.Annotated[Path, ContentType("image/*")]
upload_file = streamlit.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "bmp", "webp"])

with src_image:
=======
import enum

Image = t.Annotated[Path, ContentType("image/*")]
class UserRequestStatus(enum.Enum):
    something_went_wrong = 5
    ok = 4
    already_in_the_database = 3
    no_face_in_the_photo = 2
    is_not_registered = 1

src_image_add, dst_image_add = streamlit.columns(2)

bentoml_host = os.getenv("BENTOML_SERVICE", "http://backend:3000")


upload_file = streamlit.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "bmp", "webp"])

with src_image_add:
>>>>>>> Stashed changes
    if upload_file is not None:
        streamlit.image(upload_file, channels="BGR", width=900)
        suffix = Path(upload_file.name).suffix
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
            tmp_file.write(upload_file.getvalue())
            tmp_path = Path(tmp_file.name)
<<<<<<< Updated upstream

        with bentoml.SyncHTTPClient(bentoml_host) as client:
            result = client.render(tmp_path)

with dst_image:
    if upload_file is not None:
        streamlit.image(result, channels="BGR", width=900)
=======
            
with dst_image_add:
    if upload_file is not None:
        if streamlit.button("Add user", width="stretch"):
            with bentoml.SyncHTTPClient(bentoml_host, timeout=600) as client:

                result = client.add_user(tmp_path)

                if (result == UserRequestStatus.ok.value) :
                    streamlit.success("Пользователь добавлен в базу данных")
                    #streamlit.image(image, channels="BGR", width=300)
                elif (result == UserRequestStatus.already_in_the_database.value) :
                    streamlit.error("Пользователь уже есть в базе данных")
                elif (result == UserRequestStatus.no_face_in_the_photo.value) :
                    streamlit.warning("На фотографии нет лиц")


        if streamlit.button("Find user", width="stretch"):
            with bentoml.SyncHTTPClient(bentoml_host, timeout=600) as client:

                result = client.find_user(tmp_path)

                if (result == UserRequestStatus.ok.value) :
                    streamlit.success("Пользователь есть в базе данных")
                    #streamlit.image(image, channels="BGR", width=300)
                elif (result == UserRequestStatus.is_not_registered.value) :
                    streamlit.error("Пользователь не зарегестрирован")
                elif (result == UserRequestStatus.no_face_in_the_photo.value) :
                    streamlit.warning("На фотографии нет лиц")
>>>>>>> Stashed changes
