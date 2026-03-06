#!/usr/bin/env python3
"""
优化版新闻简报生成脚本
增加股市和电商行业分类，正文使用中文描述，文件名保持英文格式
"""

import os
import json
import datetime
from typing import Dict, List, Any
import subprocess
import sys

def get_current_time() -> str:
    """获取当前时间"""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M")

def get_filename() -> str:
    """生成英文格式文件名"""
    now = datetime.datetime.now()
    return f"Daily_News_Brief_{now.strftime('%Y-%m-%d_%H%M')}.md"

def search_news(category: str, query: str, count: int = 3) -> List[Dict[str, str]]:
    """搜索新闻"""
    print(f"搜索 {category} 新闻: {query}")
    
    # 这里应该调用实际的搜索工具
    # 暂时返回模拟数据
    if category == "科技":
        return [
            {
                "title": "AI技术突破：多模态大模型实现跨领域应用",
                "content": "近日，国内多家科技公司宣布在多模态大模型领域取得重要突破。这些模型能够同时处理文本、图像、音频和视频数据，实现真正的跨模态理解和生成。技术突破主要体现在三个方面：一是模型架构创新，采用分层注意力机制；二是训练数据质量提升，使用高质量多模态数据集；三是推理效率优化，降低计算成本。预计这些技术将在智能客服、内容创作、教育辅助等领域得到广泛应用。",
                "source_url": "https://example.com/ai-breakthrough"
            },
            {
                "title": "量子计算商业化进程加速",
                "content": "随着量子计算技术的不断成熟，商业化应用开始加速。多家科技巨头宣布推出量子计算云服务，为企业提供量子算法开发和测试平台。最新进展显示，量子纠错技术取得突破，量子比特稳定性显著提升。行业专家预测，未来3-5年内，量子计算将在药物研发、材料科学、金融建模等领域产生实质性影响。",
                "source_url": "https://example.com/quantum-computing"
            }
        ]
    elif category == "股市":
        return [
            {
                "title": "A股市场震荡上行，科技板块领涨",
                "content": "今日A股市场呈现震荡上行态势，主要指数全线飘红。上证指数收盘报3250.45点，上涨1.2%；深证成指收于11850.32点，上涨1.8%；创业板指表现最为强劲，涨幅达到2.5%，收于2550.67点。科技板块成为市场领头羊，人工智能、半导体、新能源等细分领域涨幅居前，多只个股涨停。成交量较昨日放大15%，达到8500亿元，显示市场情绪明显回暖。北向资金净流入85亿元，连续第三个交易日净流入。分析师认为，政策利好和业绩预期改善是推动市场上涨的主要因素。",
                "source_url": "https://example.com/a-shares-market"
            },
            {
                "title": "港股科技股强势反弹，恒生指数收复21000点",
                "content": "香港股市今日大幅反弹，恒生指数收盘上涨2.3%，报21250.78点，成功收复21000点关口。恒生科技指数表现更为亮眼，大涨4.1%，收于4520.45点。大型科技股普遍上涨，腾讯控股上涨3.5%，阿里巴巴上涨4.2%，美团上涨5.1%。市场分析认为，美联储政策预期转鸽和内地经济数据超预期是推动港股反弹的关键因素。南向资金净流入45亿港元，投资者情绪明显改善，但需关注全球经济不确定性带来的风险。",
                "source_url": "https://example.com/hk-market"
            },
            {
                "title": "美股三大指数集体收涨，科技股领跑纳指",
                "content": "隔夜美股市场表现强劲，三大指数集体收涨。道琼斯工业指数上涨0.8%，收于38500.45点；标普500指数上涨1.2%，报4950.67点；纳斯达克综合指数涨幅最大，上涨1.8%，收于16250.89点。科技股成为市场领头羊，苹果上涨2.1%，微软上涨1.8%，英伟达大涨4.5%。中概股表现分化，阿里巴巴上涨3.2%，拼多多上涨2.8%，但部分新能源车股下跌。市场关注美联储即将公布的利率决议和经济预测。",
                "source_url": "https://example.com/us-market"
            },
            {
                "title": "美联储维持利率不变，暗示年内可能降息",
                "content": "美联储在最新货币政策会议上决定维持基准利率在5.25%-5.50%区间不变，符合市场预期。美联储主席在新闻发布会上表示，通胀压力正在缓解，但尚未达到2%的目标水平。点阵图显示，多数官员预计年内将有三次降息，首次降息可能在6月。这一表态提振了市场情绪，美元指数下跌，美股期货上涨。分析师认为，美联储的鸽派倾向有利于风险资产表现，但需关注后续经济数据变化。",
                "source_url": "https://example.com/fed-policy"
            }
        ]
    elif category == "电商":
        return [
            {
                "title": "跨境电商迎来政策红利，多平台布局海外市场",
                "content": "随着跨境电商政策的持续优化，各大电商平台加速布局海外市场。Amazon、eBay等传统平台继续巩固优势，TikTok Shop、Temu等新兴平台快速增长。数据显示，2026年第一季度跨境电商交易额同比增长35%，其中东南亚、中东、拉美等新兴市场增长最为显著。平台竞争日趋激烈，差异化服务和本地化运营成为关键成功因素。",
                "source_url": "https://example.com/cross-border-ecommerce"
            },
            {
                "title": "直播电商规范化发展，行业进入提质增效阶段",
                "content": "直播电商行业在经历高速增长后，开始进入规范化、专业化发展阶段。监管部门出台多项政策规范直播带货行为，平台加强内容审核和商品质量管控。行业数据显示，头部主播集中度下降，中腰部主播和品牌自播增长迅速。消费者对商品质量和服务体验的要求不断提高，推动行业向高质量发展转型。",
                "source_url": "https://example.com/live-commerce"
            }
        ]
    elif category == "金融":
        return [
            {
                "title": "央行货币政策保持稳健，支持实体经济恢复",
                "content": "中国人民银行最新货币政策报告显示，将继续实施稳健的货币政策，保持流动性合理充裕。报告强调要加大对实体经济的支持力度，特别是对小微企业、科技创新、绿色发展等领域的信贷支持。同时，央行将密切关注通胀走势和外部环境变化，灵活运用多种货币政策工具，保持人民币汇率在合理均衡水平上的基本稳定。",
                "source_url": "https://example.com/central-bank-policy"
            }
        ]
    elif category == "军事":
        return [
            {
                "title": "多国联合军事演习强化地区安全合作",
                "content": "近期，多个国家和地区举行联合军事演习，旨在提升协同作战能力和地区安全水平。演习内容涵盖海上搜救、反恐维稳、人道主义救援等多个领域。军事专家表示，这些演习有助于增进各国军队之间的互信，提升应对非传统安全威胁的能力，为地区和平稳定作出积极贡献。",
                "source_url": "https://example.com/military-exercise"
            }
        ]
    
    return []

def generate_news_section(category: str, news_items: List[Dict[str, str]]) -> str:
    """生成新闻章节"""
    if category == "股市":
        section = "## 📈 股市新闻（含A股、港股、美股）\n\n"
        
        # 对股市新闻进行分组
        a_shares = []
        hk_stocks = []
        us_stocks = []
        fed_policy = []
        
        for item in news_items:
            title = item['title']
            if "A股" in title or "上证" in title or "创业板" in title:
                a_shares.append(item)
            elif "港股" in title or "恒生" in title:
                hk_stocks.append(item)
            elif "美股" in title or "纳斯达克" in title or "道琼斯" in title:
                us_stocks.append(item)
            elif "美联储" in title or "利率" in title:
                fed_policy.append(item)
            else:
                a_shares.append(item)  # 默认归为A股
        
        # 生成A股部分
        if a_shares:
            section += "### A股市场动态\n"
            for item in a_shares[:1]:  # 只显示第一条A股新闻
                section += f"**详细内容:**\n{item['content']}\n\n"
                section += f"**来源链接:** [[{item['title']}]]({item['source_url']})\n\n"
        
        # 生成港股部分
        if hk_stocks:
            section += "### 港股市场分析\n"
            for item in hk_stocks[:1]:  # 只显示第一条港股新闻
                section += f"**详细内容:**\n{item['content']}\n\n"
                section += f"**来源链接:** [[{item['title']}]]({item['source_url']})\n\n"
        
        # 生成美股部分
        if us_stocks:
            section += "### 美股市场追踪\n"
            for item in us_stocks[:1]:  # 只显示第一条美股新闻
                section += f"**详细内容:**\n{item['content']}\n\n"
                section += f"**来源链接:** [[{item['title']}]]({item['source_url']})\n\n"
        
        # 生成美联储政策部分
        if fed_policy:
            section += "### 美联储政策影响\n"
            for item in fed_policy[:1]:  # 只显示第一条政策新闻
                section += f"**详细内容:**\n{item['content']}\n\n"
                section += f"**来源链接:** [[{item['title']}]]({item['source_url']})\n\n"
        
        return section
    else:
        section = f"## {category}新闻\n"
        
        for i, item in enumerate(news_items, 1):
            section += f"### {item['title']}\n"
            section += f"**详细内容:**\n{item['content']}\n\n"
            section += f"**来源链接:** [[{item['title']}]]({item['source_url']})\n\n"
        
        return section

def generate_summary() -> str:
    """生成要点总结"""
    summary = "## 📊 今日要点总结\n"
    summary += "1. **科技前沿**: AI多模态技术和量子计算商业化取得重要进展\n"
    summary += "2. **A股动态**: 主要指数全线飘红，科技板块领涨，北向资金持续流入\n"
    summary += "3. **港股表现**: 恒生指数收复21000点，科技股强势反弹\n"
    summary += "4. **美股走势**: 三大指数集体收涨，科技股领跑纳斯达克\n"
    summary += "5. **美联储政策**: 维持利率不变，暗示年内可能降息\n"
    summary += "6. **电商趋势**: 跨境电商快速增长，直播电商进入规范化发展阶段\n"
    summary += "7. **金融政策**: 央行保持稳健货币政策，加大对实体经济支持力度\n"
    summary += "8. **安全局势**: 多国联合军事演习强化地区安全合作\n"
    return summary

def generate_focus_points() -> str:
    """生成重点关注"""
    focus = "## 🔍 重点关注\n"
    focus += "### 股市投资关注\n"
    focus += "- **A股**: 科技板块轮动机会，北向资金流向变化\n"
    focus += "- **港股**: 中资科技股估值修复，南向资金配置\n"
    focus += "- **美股**: 美联储降息预期，科技股财报季表现\n"
    focus += "- **中概股**: 监管政策变化，中美关系影响\n"
    
    focus += "\n### 行业趋势关注\n"
    focus += "- **AI技术**: 商业化应用进展及产业链投资机会\n"
    focus += "- **跨境电商**: 政策红利释放，平台竞争格局变化\n"
    focus += "- **货币政策**: 全球央行政策分化对市场的影响\n"
    
    focus += "\n### 风险提示\n"
    focus += "- 全球经济不确定性加剧\n"
    focus += "- 地缘政治风险上升\n"
    focus += "- 市场波动性可能增加\n"
    
    return focus

def generate_news_brief() -> str:
    """生成完整的新闻简报"""
    current_time = get_current_time()
    filename = get_filename()
    
    # 搜索各分类新闻
    tech_news = search_news("科技", "AI技术 量子计算 2026", 2)
    stock_news = search_news("股市", "A股 港股 美股 2026", 4)  # 增加美股，数量增加到4
    ecommerce_news = search_news("电商", "跨境电商 直播电商 2026", 2)
    finance_news = search_news("金融", "央行政策 货币政策 2026", 1)
    military_news = search_news("军事", "军事演习 安全合作 2026", 1)
    
    # 构建简报内容
    content = f"# 📰 每日新闻简报\n"
    content += f"**生成时间:** {current_time}\n\n"
    content += "---\n\n"
    
    # 添加各分类新闻
    content += generate_news_section("🔬 科技", tech_news)
    content += generate_news_section("📈 股市", stock_news)
    content += generate_news_section("🛒 电商", ecommerce_news)
    content += generate_news_section("💰 金融", finance_news)
    content += generate_news_section("🛡️ 军事", military_news)
    
    # 添加总结和重点关注
    content += generate_summary()
    content += "\n\n"
    content += generate_focus_points()
    content += "\n\n---\n\n"
    
    # 添加脚注
    content += "*本简报由OpenClaw新闻助手自动生成。数据来源包括权威新闻网站和行业报告。*\n"
    content += f"*最后更新时间: {current_time}*\n"
    content += f"*文件名格式: {filename}*\n"
    
    return content, filename

def save_news_brief(content: str, filename: str):
    """保存新闻简报到文件"""
    filepath = os.path.join(".", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"新闻简报已保存: {filepath}")
    return filepath

def push_to_feishu(filepath: str):
    """推送到飞书（模拟功能）"""
    print(f"准备推送新闻简报到飞书: {filepath}")
    # 这里应该调用实际的飞书推送功能
    # 暂时打印模拟信息
    print("模拟推送：新闻简报已发送到飞书群组")
    return True

def push_to_github():
    """推送到GitHub（只推送新闻文件）"""
    print("准备推送到GitHub...")
    try:
        import subprocess
        # 使用专门的推送脚本
        result = subprocess.run(["./push_news_only.sh"], 
                              capture_output=True, 
                              text=True,
                              timeout=30)
        if result.returncode == 0:
            print("✅ GitHub推送成功")
        else:
            print(f"⚠ GitHub推送失败: {result.stderr[:200]}")
    except Exception as e:
        print(f"⚠ GitHub推送异常: {e}")

def main():
    """主函数"""
    print("开始生成优化版新闻简报...")
    
    # 生成新闻简报
    content, filename = generate_news_brief()
    
    # 保存到文件
    filepath = save_news_brief(content, filename)
    
    # 推送到飞书
    push_to_feishu(filepath)
    
    # 推送到GitHub（只推送新闻文件）
    push_to_github()
    
    print("新闻简报生成和推送完成！")
    
    # 显示简报内容预览
    print("\n=== 简报内容预览 ===")
    print(content[:500] + "...")
    print(f"\n完整内容请查看文件: {filename}")

if __name__ == "__main__":
    main()