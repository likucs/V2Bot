from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
<b>Hey</b><b> {} </b>

<b>I am Telegram Most Powerful Url Uploader Bot</b>

<b>I can Upload Any Link in File or Video</b>

<b>Use Help Command to Know How to Use me</b>

<b>Made With ð By</b><b> @cs_cloud</b>
"""
    HELP_TEXT = """
<b>Link to Media or File</b>
â  <b>Send a link for upload to telegram file or media.</b>

<b>Set Thumbnail</b>
â  <b>Send a photo to make it as permanent thumbnail.</b>

<b>Deleting Thumbnail</b>
â  Send /del_thumb to delete thumbnail.</b>

<b>Show Thumbnail</b>
â  Send /show_thumb to view custom thumbnail.</b>

<b>Convert To Video</b>
â  <b>Send /convert2video to Convert File In Video</b>

<b>Convert To File</b>
â  <b>Send /c2file To Convert Video To File</b>

<b>Upload To GoFile</b>
â  Send /uptogofile To Upload Media On GoFile.</b>

<b>Upload To Anonfiles</b>
â  Send /uptoanonfile .</b>

<b>Made With ð By</b><b> @iAmLiKu1</b>
"""
    ABOUT_TEXT = """                   
 **ð¤ <b>Bot :** URL Uploader</b>\n
 **ð² <b>Developer :** [Cs LÉªá´á´](https://telegram.me/iAmLiKu1)</b>\n
 **ð¥ <b>Channel :** [Tellybots_4u](https://telegram.me/cs_cloud)</b>\n
 **âï¸ <b>Credits :** Everyone in this journey</b>\n
 **ð´ <b>Source :** [Click here](https://t.me/cs_cloud)</b>\n
 **ð <b>Language :** [Python3](https://python.org)</b>\n
 **ð <b>Library :** [Pyrogram v1.2.0](https://pyrogram.org)</b>\n
 **ð <b>Server :** [Heroku](https://heroku.com)</b>\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ð¢ Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('ð Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('ð¤§ Help', callback_data='help'),
        InlineKeyboardButton('ð Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ð¡ Home', callback_data='home'),
        InlineKeyboardButton('ð² About', callback_data='about'),
        InlineKeyboardButton('â Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ð¡ Home', callback_data='home'),
        InlineKeyboardButton('â Help', callback_data='help'),
        InlineKeyboardButton('â Close', callback_data='close')
        ]]
    )
    IFLONG_FILE_NAME = " Only 64 characters can be named . "
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>No preminum plans available in this bot </b>  /help for Details"
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>File size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_FILE = " ð¥DownloadinGð¥ File "
    UPLOAD_FILE = " ð¤UploadinGð¤ \n\n To  transfer.sh "
    ANNO_UPLOAD = " ð¤UploadinGð¤ \n\n To  anonfiles.com "
    BAY_UPLOAD = " ð¤UploadinGð¤ \n\n To  bayfiles.com "
    GO_FILE_UPLOAD = " ð¤UploadinGð¤ \n\n To  gofile.io "
    DOWNLOAD_START = " ð¥DownloadinGð¥ \n\nWaitâ³ until it completed."
    UPLOAD_START = " ð¤UploadinGð¤ "
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "By @Tellybots_4u"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\n\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/ThankTelegram'>@iAmLiKu1</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "â Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "â Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    NO_VOID_FORMAT_FOUND = "ERROR... {}"
    FILE_NOT_FOUND = "Error, File not Found!!"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """About you...
--------
Telegram ID : <code>{}</code>
"""
    HELP_USER = """Hii I am <b>Multipurpose bot</b> and I can perform many tasks.
    
1.) Send url (Link|New Name with Extension).
2.) Send Custom Thumbnail (Optional).
3.) Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots

JOIN : https://t.me/TGBotsCollection \n For the List of Telegram Bots"""
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /ren with custom thumbnail support"
    AFTER_GET_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>â¡Linkâ¡ :</b> <code>{}</code>\n\nJoin : @cs_cloud"
    AFTER_GET_DL_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>â¡Linkâ¡ :</b> <code>{}</code>\n\nValid for <b>14</b> days.\nJoin : @cs_cloud"
    #AFTER_GET_DL_LINK = " {} valid for 30 or more days.\n\n Join : @cs_cloud \n For the list of Telegram bots. "
    AFTER_GET_GOFILE_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n<b>File MD5 Checksum :</b> <code>{}</code>\n\n<b>â¡Linkâ¡ :</b> <code>{}</code>\n\n Valid untill 10 days of inactivity\nJoin : @cs_cloud"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS for screenshot of that specific time."""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Join : @cs_cloud \n For the list of Telegram bots. "
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. â ï¸ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@iAmLiKu1</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    CHECKING_LINK = "<code>Analysing Your Link</code>â³"
