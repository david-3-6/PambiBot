from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import asyncio

TOKEN = "6774136454:AAHHwHmCXBe-JWbJeB79SLb-KoyDFjoI450"
GROUP_ID = "-1002147496977"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [
            InlineKeyboardButton("Show Rules", callback_data='show_rules'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f'Hello, Hola, Hallo, Olá, नमस्ते, こんにちわ, 你好, Здравствуйте {user.first_name}!\n\n🇺🇸 Please click the button to view the group rules.\n\n🇪🇸 Por favor, pulsa el botón para ver las reglas del grupo.\n\n🇩🇪 Bitte klicken Sie auf die Schaltfläche, um die Gruppenregeln anzuzeigen.\n\n🇧🇷 🇵🇹 Clique no botão para ver as regras do grupo.\n\n🇮🇳 समूह के नियम देखने के लिए कृपया बटन दबाएँ।\n\n🇯🇵 ボタンをクリックしてグループ規則をご覧ください。\n\n🇨🇳 请点击按钮查看小组规则\n\n🇷🇺 Нажмите на кнопку, чтобы просмотреть правила группы.\n\n🇰🇷 그룹 규칙을 보려면 버튼을 클릭하세요.', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "show_rules":
        #En ingles:
        await context.bot.send_message(chat_id=query.from_user.id, text="🇺🇸 Rules:\n\n1. By accepting these rules and notices you confirm that you have reached the age of majority (normally in all countries +18 years) and are of the required age to invest in the market.\n\n2. By accepting the rules you accept that any message in the group from a moderator is not inciting to buy any cryptocurrency, only investment advice or mere objective information. Remember that many people who invest, lose money. Each member has the right to make their own investment decisions.\n\n3. Do not send any illegal content in the group (illegal sale of weapons, illegal sale of drugs, child pornography, ...). If you do not comply you will be immediately banned forever.\n\n4. Sending content different from the topic for which the group was made may be grounds for penalty, even expulsion, depending on the severity.\n\n5. Maintain respect among all users.\n\n6. Spam, referral links, and repetitive messages are not allowed.\n\n7. Verification of Information: Before sharing news or information, members should verify the source and accuracy of the information. Sharing false or misleading information may result in a warning or expulsion.")
        #En español:
        await context.bot.send_message(chat_id=query.from_user.id, text="🇪🇸 Normas:\n\n1. Al aceptar estas reglas y avisos confirmas que has alcanzado la mayoría de edad (normalmente en todos los países +18 años) y tienes la edad requerida para invertir en el mercado.\n\n2. Al aceptar las normas aceptas que cualquier mensaje en el grupo por parte de un moderador no incita a comprar ninguna criptodivisa, sólo consejos de inversión o mera información objetiva. Recuerda que mucha gente que invierte, pierde dinero. Cada miembro tiene derecho a tomar sus propias decisiones de inversión. No envíes ningún contenido ilegal en el grupo (venta ilegal de armas, venta ilegal de drogas, pornografía infantil, ...). Si no lo cumples serás inmediatamente baneado para siempre.\n\n4. Enviar contenido diferente al tema para el que se hizo el grupo puede ser motivo de sanción, incluso expulsión, dependiendo de la gravedad.\n\n5. Mantener el respeto entre todos los usuarios.\n6. No se permite el spam, los enlaces de referencia ni los mensajes repetitivos.\n\n7. Verificación de la información: Antes de compartir noticias o información, los miembros deben verificar la fuente y la exactitud de la información. Compartir información falsa o engañosa puede dar lugar a una advertencia o expulsión.")
        #Alemán:
        await context.bot.send_message(chat_id=query.from_user.id, text="🇩🇪 Regeln:\n\n1. Durch die Annahme dieser Regeln und Hinweise bestätigen Sie, dass Sie die Volljährigkeit erreicht haben (normalerweise in allen Ländern +18 Jahre) und das erforderliche Alter haben, um in den Markt zu investieren.\n\n2. Durch die Annahme der Regeln akzeptieren Sie, dass jede Nachricht eines Moderators in der Gruppe keine Aufforderung zum Kauf einer Kryptowährung darstellt, sondern lediglich eine Anlageberatung oder eine rein objektive Information. Denken Sie daran, dass viele Menschen, die investieren, Geld verlieren. Jedes Mitglied hat das Recht, seine eigenen Investitionsentscheidungen zu treffen.\n\n3. Versenden Sie keine illegalen Inhalte in der Gruppe (illegaler Verkauf von Waffen, illegaler Verkauf von Drogen, Kinderpornographie, ...). Wenn Sie sich nicht daran halten, werden Sie sofort für immer gesperrt.\n\n4. Das Versenden von Inhalten, die nicht dem Thema entsprechen, für das die Gruppe eingerichtet wurde, kann je nach Schweregrad eine Strafe oder sogar den Ausschluss zur Folge haben.\n\n5. Achten Sie auf den Respekt zwischen allen Benutzern.\n\n6. Spam, Empfehlungslinks und sich wiederholende Nachrichten sind nicht erlaubt.\n\n7. Überprüfung von Informationen: Bevor Nachrichten oder Informationen weitergegeben werden, sollten die Mitglieder die Quelle und die Richtigkeit der Informationen überprüfen. Die Weitergabe falscher oder irreführender Informationen kann zu einer Verwarnung oder einem Ausschluss führen.")
        #Portugués:
        await context.bot.send_message(chat_id=query.from_user.id, text="🇧🇷 🇵🇹 Regras:\n\n1. Ao aceitar estas regras e avisos, confirma que atingiu a maioridade (normalmente em todos os países +18 anos) e que tem a idade necessária para investir no mercado.\n\n2. Ao aceitar as regras, aceita que qualquer mensagem no grupo de um moderador não é um incitamento à compra de qualquer criptomoeda, apenas um conselho de investimento ou mera informação objetiva. Lembre-se que muitas pessoas que investem, perdem dinheiro. Cada membro tem o direito de tomar as suas próprias decisões de investimento.\n3. Não enviar qualquer conteúdo ilegal no grupo (venda ilegal de armas, venda ilegal de drogas, pornografia infantil, ...). Se não cumprires serás imediatamente banido para sempre.\n\n4. O envio de conteúdo diferente do tópico para o qual o grupo foi criado pode ser motivo de penalização, até mesmo expulsão, dependendo da gravidade.\n\n5. Manter o respeito entre todos os utilizadores.\n\n6. Spam, links de referência e mensagens repetitivas não são permitidos.\n\n7. Verificação de informações: Antes de partilhar notícias ou informações, os membros devem verificar a fonte e a exatidão das informações. A partilha de informações falsas ou enganosas pode resultar num aviso ou expulsão.")
        #Indio
        await context.bot.send_message(chat_id=query.from_user.id, text="🇮🇳 नियम:\n\n1. इन नियमों और नोटिसों को स्वीकार करके आप पुष्टि करते हैं कि आप वयस्कता की आयु (सामान्य रूप से सभी देशों में +18 वर्ष) तक पहुंच गए हैं और बाजार में निवेश करने के लिए आवश्यक आयु के हैं।\n\n2. नियमों को स्वीकार करके आप स्वीकार करते हैं कि समूह में मॉडरेटर का कोई भी संदेश किसी क्रिप्टोकरेंसी को खरीदने के लिए उकसाने वाला नहीं है, केवल निवेश सलाह या मात्र वस्तुनिष्ठ जानकारी है। याद रखें कि निवेश करने वाले बहुत से लोग अपना पैसा खो देते हैं। प्रत्येक सदस्य को अपने निवेश निर्णय लेने का अधिकार है।\n\n3. समूह में कोई भी अवैध सामग्री (हथियारों की अवैध बिक्री, दवाओं की अवैध बिक्री, बाल अश्लीलता, ...) न भेजें। यदि आप इसका अनुपालन नहीं करते हैं तो आपको तुरंत हमेशा के लिए प्रतिबंधित कर दिया जाएगा।\n\n4. जिस विषय के लिए समूह बनाया गया था उससे भिन्न सामग्री भेजना गंभीरता के आधार पर दंड, यहां तक ​​कि निष्कासन का आधार भी हो सकता है।\n\n5. सभी उपयोगकर्ताओं के बीच सम्मान बनाए रखें.\n\n6. स्पैम, रेफरल लिंक और दोहराए जाने वाले संदेशों की अनुमति नहीं है।\n\n7. सूचना का सत्यापन: समाचार या जानकारी साझा करने से पहले, सदस्यों को जानकारी के स्रोत और सटीकता का सत्यापन करना चाहिए। गलत या भ्रामक जानकारी साझा करने पर चेतावनी या निष्कासन हो सकता है।")
        #japones
        await context.bot.send_message(chat_id=query.from_user.id, text="🇯🇵 ルール\n\n1. この規則と注意事項に同意することにより、あなたは成年（通常すべての国で18歳以上）に達しており、市場に投資するために必要な年齢であることを確認します。\n\n2. 2.本規則に同意することで、あなたは、グループ内のモデレーターからのいかなるメッセージも、暗号通貨の購入を扇動するものではなく、投資アドバイスまたは単なる客観的な情報であることを承諾するものとします。投資する多くの人がお金を失うことを忘れないでください。各メンバーは、自分自身の投資判断を下す権利を持っています。\n\n3. 3.グループ内で違法な内容（武器の違法販売、薬物の違法販売、児童ポルノなど）を送信しないでください。従わない場合、直ちに永久追放となります。\n\n4. グループが作成されたトピックと異なるコンテンツを送信すると、ペナルティーの対象となる場合があります。\n\n5. すべての利用者に敬意を払いましょう。\n\n6. スパム、紹介リンク、繰り返しのメッセージは禁止されています。\n\n7. 情報の検証： 情報の確認：ニュースや情報を共有する前に、メンバーは情報の出所と正確性を確認する。虚偽または誤解を招くような情報を共有すると、警告または除名されることがあります。")
        #Chino
        await context.bot.send_message(chat_id=query.from_user.id, text="🇨🇳 规则：\n\n1. 接受这些规则和通知即表示您确认您已达到法定年龄（在所有国家通常为 18 岁以上），并且达到了在市场上进行投资所需的年龄。\n\n2. 接受本规则，即表示您接受版主在群组中发布的任何消息均非煽动购买任何加密货币，仅为投资建议或客观信息。请记住，很多人投资后都会亏钱。每个成员都有权做出自己的投资决定。\n\n3. 不要在群组中发送任何非法内容（非法销售武器、非法销售毒品、儿童色情等）。如果您不遵守，您将被立即永久封禁。\n\n4. 4. 发送与群组主题不同的内容可能会受到处罚，甚至被驱逐，视情节轻重而定。\n\n5. 保持对所有用户的尊重。\n\n6. 禁止垃圾邮件、推荐链接和重复信息。\n\n7. 核实信息： 在分享新闻或信息之前，会员应核实信息的来源和准确性。分享虚假或误导性信息可能导致警告或开除。")
        #Ruso
        await context.bot.send_message(chat_id=query.from_user.id, text="🇷🇺 Правила:\n\n1. Принимая эти правила и уведомления, вы подтверждаете, что достигли совершеннолетия (обычно во всех странах +18 лет) и являетесь лицом, достигшим возраста, необходимого для инвестирования в рынок.\n\n2. Принимая правила, вы соглашаетесь с тем, что любое сообщение в группе от модератора не является призывом к покупке какой-либо криптовалюты, а лишь инвестиционным советом или просто объективной информацией. Помните, что многие люди, которые инвестируют, теряют деньги. Каждый участник имеет право принимать свои собственные инвестиционные решения.\n\n3. Не отправляйте в группу никакого незаконного контента (незаконная продажа оружия, незаконная продажа наркотиков, детская порнография, ...). Если вы не выполните это требование, вы будете немедленно забанены навсегда.\n\n4. Отправка контента, отличающегося от темы, для которой была создана группа, может стать основанием для наказания, вплоть до исключения, в зависимости от степени тяжести.\n\n5. Поддерживайте уважение между всеми пользователями.\n\n6. Спам, реферальные ссылки и повторяющиеся сообщения не допускаются.\n\n7. Проверка информации: Прежде чем делиться новостями или информацией, пользователи должны проверить источник и точность информации. Распространение ложной или вводящей в заблуждение информации может привести к предупреждению или исключению.")
        #Coreano
        await context.bot.send_message(chat_id=query.from_user.id, text="규칙:\n\n1. 이러한 규칙과 고지에 동의함으로써 귀하는 성년(일반적으로 모든 국가에서 +18세 이상)이 되었으며 시장에 투자할 수 있는 연령에 도달했음을 확인합니다.\n\n2. 이 규칙에 동의함으로써 귀하는 운영자가 그룹에서 보내는 모든 메시지가 암호화폐 구매를 유도하는 것이 아니라 투자 조언이나 단순한 객관적인 정보임을 수락하는 것입니다. 투자한 많은 사람들이 손실을 본다는 사실을 기억하세요. 각 회원은 스스로 투자 결정을 내릴 권리가 있습니다.\n\n3. 그룹 내에서 불법 콘텐츠(불법 무기 판매, 불법 마약 판매, 아동 음란물 등)를 보내지 마세요. 이를 준수하지 않을 경우 즉시 영구 금지됩니다.\n\n4. 그룹이 만들어진 주제와 다른 콘텐츠를 전송하는 것은 심각도에 따라 처벌, 심지어 퇴출의 사유가 될 수 있습니다.\n\n5. 모든 사용자 간에 존중을 유지합니다.\n\n6. 스팸, 추천 링크 및 반복적인 메시지는 허용되지 않습니다.\n\n7. 정보 확인: 회원은 뉴스나 정보를 공유하기 전에 정보의 출처와 정확성을 확인해야 합니다. 허위 또는 오해의 소지가 있는 정보를 공유하면 경고 또는 제명될 수 있습니다.")
        keyboard = [
            [
                InlineKeyboardButton("Accept rules 👍✅", callback_data='1'),
                InlineKeyboardButton("Reject rules 👎❌", callback_data='2'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=query.from_user.id, text="🇺🇸 Please accept (left button) or reject the rules (right button)\n\n🇪🇸 Por favor, acepta (botón izquierdo) o rechaza las normas (botón derecho)\n\n🇩🇪 Bitte akzeptieren Sie (linker Knopf) oder lehnen Sie die Regeln ab (rechter Knopf)\n\n🇧🇷 🇵🇹 Por favor, aceite (botão esquerdo) ou rejeite as regras (botão direito)\n\n🇮🇳 कृपया स्वीकार करें (बाएं बटन) या नियमों को अस्वीकार करें (दाएं बटन)\n\n🇯🇵 ルールを承認してください（左ボタン）または拒否してください（右ボタン）\n\n🇨🇳 请接受（左按钮）或拒绝规则（右按钮）\n\n🇷🇺 Пожалуйста, примите (левая кнопка) или отклоните правила (правая кнопка)\n\n🇰🇷 규칙을 수락하십시오 (왼쪽 버튼) 또는 거부하십시오 (오른쪽 버튼)", reply_markup=reply_markup)

    elif query.data == "1":
        await context.bot.send_message(chat_id=query.from_user.id, text="Welcome, ¡Bienvenido!, Willkommen, Bem-vindo, स्वागत है, ようこそ, 欢迎, Добро пожаловать, 환영합니다")
        await context.bot.restrict_chat_member(chat_id=GROUP_ID, user_id=query.from_user.id, permissions=ChatPermissions(can_send_messages=True))
    elif query.data == "2":
        await context.bot.send_message(chat_id=query.from_user.id, text="🇺🇸 We're sorry, you can't be in our group\n\n🇪🇸 Lo sentimos, no puede estar en nuestro grupo\n\n🇩🇪 Es tut uns leid, Sie können nicht in unserer Gruppe sein\n\n🇧🇷 🇵🇹 Lamentamos, você não pode estar em nosso grupo\n\n🇮🇳 हमें खेद है, आप हमारे समूह में नहीं हो सकते\n\n🇯🇵 申し訳ありませんが、あなたは私たちのグループに参加できません\n\n🇨🇳 对不起，你不能在我们的组中\n\n🇷🇺 Мы сожалеем, но вы не можете быть в нашей группе\n\n🇰🇷 죄송합니다, 우리 그룹에 있을 수 없습니다")
        await context.bot.ban_chat_member(chat_id=GROUP_ID, user_id=query.from_user.id)

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for new_user_obj in update.message.new_chat_members:
        new_user = '@' + new_user_obj['username'] if new_user_obj['username'] else new_user_obj['first_name']
        keyboard = [
            [
                InlineKeyboardButton("Talk with me", url='https://t.me/PambiCoinBot'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=GROUP_ID, text=f"Welcome, ¡Bienvenido!, Willkommen, Bem-vindo, स्वागत है, ようこそ, 欢迎, Добро пожаловать, 환영합니다\n\n {new_user},\n\n🇺🇸 Talk to pambiBot to interact in the group\n\n🇪🇸 Habla con pambiBot para interactuar en el grupo\n\n🇩🇪 Sprechen Sie mit pambiBot, um in der Gruppe zu interagieren\n\n🇧🇷 🇵🇹 Fale com o pambiBot para interagir no grupo\n\n🇮🇳 समूह में बातचीत करने के लिए pambiBot से बात करें\n\n🇯🇵 グループでやり取りするためにpambiBotと話す\n\n🇨🇳 与pambiBot交谈以在组中互动\n\n🇷🇺 Поговорите с pambiBot, чтобы взаимодействовать в группе\n\n🇰🇷 그룹에서 상호 작용하기 위해 pambiBot와 대화하세요", reply_markup=reply_markup)
        await context.bot.restrict_chat_member(chat_id=GROUP_ID, user_id=new_user_obj['id'], permissions=ChatPermissions(can_send_messages=False))
        await asyncio.sleep(900)  # Aquí está la corrección
        user_status = await context.bot.get_chat_member(chat_id=GROUP_ID, user_id=new_user_obj['id'])
        if not user_status['can_send_messages']:
            await context.bot.ban_chat_member(chat_id=GROUP_ID, user_id=new_user_obj['id'])  # Aquí está la corrección

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button))
application.run_polling(allowed_updates=Update.ALL_TYPES)
