# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Merhaba 👋 [{}](tg://user?id={})!**\n\n Ben gruplarınızda spam önleyici olarak  @combot un bir yardımcısıyım ne yapabildiğimj bilmek istiyorsan /help yaz ."
      HELP_MSG = [
        ".",
'''''
Beni Grubuna ekle ve yönetici yap:

- Grubundaki spam yapmaya çalışanları daha yapmaya başlarken fark ederim.
-Grubunuzu kötü hackırlardan korurum.
-Grubunuzu Dünya ve Türkiye sıralamasına sokarak grubunuzun büyümesine yardım ederim.
- İlerleyen zamanlarda grubunuzun reklamını yapıp üyelerinizin çoğalmasına yardım ederim.

# Tek yapmanız gereken beni grubunuzda yönetici yapmak geri kalanını bana bırak:)
'''''
      ]
