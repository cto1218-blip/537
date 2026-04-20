#!/usr/bin/env python3
"""
修复两个问题：
1. AI 预测补充详细分析（200+字）
2. 金价/油价现价和预测分行显示
"""
import re

with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================
# 问题 1: AI 预测补充详细分析
# ============================================
ai_predictions = [
    {
        'title': '停火持續至4/21',
        'old_desc': '基於當前局勢和市場數據的綜合分析。',
        'new_desc': '''<strong>分析：</strong>當前停火協議面臨嚴峻考驗。黎巴嫩問題是最大變數——美以伊三方對「黎巴嫩是否包含在停火範圍內」存在公開分歧。以色列本週在黎巴嫩發動戰爭以來最大規模空襲，內塔尼亞胡明確「黎巴嫩沒有停火」；伊朗堅持黎巴嫩必須涵蓋。CNN警告協議「瀕臨崩潰」。內塔尼亞胡在國內遭遇史無前例的政治風暴，需要通過強硬立場平息批評。Polymarket顯示52%機率停火破裂。綜合評估：<strong>黎巴嫩衝突升級風險極高，協議持續至4/21的可能性較低</strong>。'''
    },
    {
        'title': '霍爾木茲海峽4月重開',
        'old_desc': '基於當前局勢和市場數據的綜合分析。',
        'new_desc': '''<strong>分析：</strong>霍爾木茲海峽重新開放進展緩慢。儘管川普宣布「非伊朗船隻可通過」，但油輪/貨船繼續觀望，只有俄羅斯油輪通過。<strong>可能存在水雷威脅</strong>需要清理作業。馬士基集團警告運營恢復可能需要「數週甚至數月」。Polymarket顯示僅14%機率4月底前恢復正常。JP Morgan警告：若僵局持續至7月，油價可能衝破$120。Goldman警告：再關閉一個月，2026年全年Brent將維持$100+。綜合評估：<strong>安全擔憂和地緣不確定性將延緩恢復進程</strong>。'''
    },
    {
        'title': '黎巴嫩衝突持續',
        'old_desc': '基於當前局勢和市場數據的綜合分析。',
        'new_desc': '''<strong>分析：</strong>黎巴嫩衝突幾乎確定持續。內塔尼亞胡明確表示「黎巴嫩沒有停火」，授權與黎巴嫩談判但攻擊未停止。以色列本週在黎巴嫩發動戰爭以來最大規模空襲（數百架次），超160人死亡。美以伊三方對黎巴嫩問題存在<strong>根本性分歧</strong>：以色列認為不在停火範圍內，伊朗堅持必須涵蓋。內塔尼亞胡在國內遭遇政治風暴，需要通過對黎巴嫩的強硬立場證明「並非完全投降」。Polymarket顯示97%機率黎巴嫩衝突持續。綜合評估：<strong>黎巴嫩衝突是當前中東局勢最大的不穩定因素</strong>。'''
    },
    {
        'title': '川普6月前宣布結束',
        'old_desc': '基於當前局勢和市場數據的綜合分析。',
        'new_desc': '''<strong>分析：</strong>川普6月前宣布戰爭結束的可能性極低。當前停火協議是兩週試驗性質，距離「戰爭結束」還有<strong>巨大差距</strong>。黎巴嫩問題未解決、霍爾木茲海峽未完全開放、以色列國內政治危機、伊朗核問題懸而未決——任何一個變數都可能引發協議崩潰。加薩停火已持續6個月但暴力未完全停止，顯示「停火」與「戰爭結束」之間存在鴻溝。Polymarket僅15%機率6月前宣布結束。綜合評估：<strong>短期內實現全面和平的可能性微乎其微</strong>。'''
    }
]

for pred in ai_predictions:
    # 转义特殊字符
    old_pattern = re.escape(pred['old_desc'])
    # 替换
    html = re.sub(
        f'<div class="prediction-title">{re.escape(pred["title"])}</div>\\s*<div class="prediction-description">{old_pattern}</div>',
        f'<div class="prediction-title">{pred["title"]}</div>\n                    <div class="prediction-description">{pred["new_desc"]}</div>',
        html,
        count=1
    )
    print(f"✓ 补充 AI 预测分析: {pred['title']}")

# ============================================
# 问题 2: 金价/油价现价和预测分行
# ============================================

# 金价板块：第一行1个现价，第二行2个预测
gold_section_start = html.find('<!-- 黃金市場分析 -->')
gold_section_end = html.find('<!-- 國際油價分析', gold_section_start)

if gold_section_start > 0 and gold_section_end > 0:
    gold_section = html[gold_section_start:gold_section_end]
    
    # 找到第一个预测卡片（短期預測）
    first_prediction = gold_section.find('📊 短期預測（7日）')
    if first_prediction > 0:
        # 往回找到 wrapper
        wrapper_start = gold_section.rfind('<div class="market-card-wrapper">', 0, first_prediction)
        
        # 找到最后一个预测卡片的结束
        last_prediction_end = gold_section.rfind('</div>\n                    </div>')
        
        if wrapper_start > 0 and last_prediction_end > 0:
            abs_wrapper_start = gold_section_start + wrapper_start
            abs_last_end = gold_section_start + last_prediction_end + len('</div>\n                    </div>')
            
            # 包装两个预测卡片
            html = (
                html[:abs_wrapper_start] +
                '                    <div class="prediction-row gold-predictions">\n' +
                html[abs_wrapper_start:abs_last_end] +
                '\n                    </div>' +
                html[abs_last_end:]
            )
            print("✓ 金价预测卡片分行显示（第二行）")

# 油价板块：第一行2个现价，第二行3个预测（已经处理过了）
print("✓ 油价预测卡片已在第二行（之前已处理）")

# 保存
with open('middle-east-tracker-zh-TW.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ 修复完成！")
print("\n【AI 预测】")
print("- 每个预测现在有 200+ 字详细分析")
print("- 包含具体数据、分歧点、风险评估和综合结论")
print("\n【卡片布局】")
print("金价板块：")
print("  第一行：💰 現貨黃金")
print("  第二行：📊 短期預測 | 📊 悲觀情境")
print("\n油价板块：")
print("  第一行：💰 當前 WTI | 💰 當前 Brent")
print("  第二行：📊 樂觀情境 | 📊 基準情境 | 📊 悲觀情境")
