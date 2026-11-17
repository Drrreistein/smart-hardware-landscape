#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按自动驾驶图谱首页的实现方式，为多个行业生成同款单文件交互式站点。"""
import os, re, html, json, shutil

BASE = '/Users/a1-6/WorkBuddy/2026-10-21-16-35-12'
TPL = os.path.join(BASE, 'auto-driving-map', 'index.html')
OUT = os.path.join(BASE, 'sites')

# 复用原站的 CSS
src = open(TPL, encoding='utf-8').read()
CSS = re.search(r'<style>(.*?)</style>', src, re.S).group(1)

# ---------- 数据格式：名称|环节codes|技术codes|场景codes|报告或-|玩家模式 ----------
RAW = {}

RAW['embodied'] = """
绿的谐波|u1|WH,WR|工业制造|-|part
双环传动|u1|WH,WR|工业制造|-|part
中大力德|u1|WH,WR|工业制造|-|part
哈默纳科|u1|WH|工业制造|-|part
贝斯特|u2|WH|工业制造|-|part
恒立液压|u2|WH|工业制造|-|part
五洲新春|u2|WH|工业制造|-|part
秦川机床|u2|WH|工业制造|-|part
舍弗勒|u2|WH|工业制造|-|part
鸣志电器|u3|WH,QU|工业制造,科研教育|-|part
伟创电气|u3|WH|工业制造|-|part
步科股份|u3|WH|工业制造|-|part
江苏雷利|u3|WH|工业制造|-|part
鼎智科技|u3|WH|工业制造|-|part
柯力传感|u4|WH,WA|工业制造,仓储物流|-|part
东华测试|u4|WH|工业制造|-|part
坤维科技|u4|WH,WA|工业制造|-|part
宇立仪器|u4|WH|工业制造|-|part
蓝点触控|u4|WH,WA|工业制造|-|part
奥比中光|u5|WH,HW,WA|工业制造,商用服务,科研教育|-|part
图漾科技|u5|WH,WA|工业制造,仓储物流|-|part
舜宇光学|u5|WH|工业制造|-|part
韦尔股份|u5|WH|工业制造|-|part
梅卡曼德机器人|u5,m9|WA,SP|工业制造,仓储物流|梅卡曼德机器人-首次覆盖报告|part
兆威机电|u6|WH|工业制造|-|part
因时机器人|u6|WH|工业制造|-|part
傲意科技|u6|WH|医疗健康|-|part
灵心巧手|u6|WH|科研教育|-|part
英伟达|u7,s1|WH,HW,WA,QU,SP|科研教育,工业制造|-|part
地平线机器人|u7|WH,HW|工业制造,科研教育|地平线机器人-首次覆盖报告|part
瑞芯微|u7|WH,SP|商用服务,家庭|-|part
全志科技|u7|SP|家庭|-|part
华为昇腾|u7,s1|WH,HW|工业制造,科研教育|-|part
寒武纪|u7|WH|科研教育|-|part
黑芝麻智能|u7|HW|工业制造|-|part
宁德时代|u8|WH|工业制造|-|part
亿纬锂能|u8|WH|工业制造|-|part
旭升集团|u8|WH|工业制造|-|part
爱柯迪|u8|WH|工业制造|-|part
长光华芯|u9|WH|工业制造|-|part
源杰科技|u9|WH|工业制造|-|part
世运电路|u9|WH|工业制造|世运电路-首次覆盖报告|part
智元机器人|m1,d5|WH,HW|工业制造,仓储物流,文娱商演|-|oem
宇树科技|m1,m3,d4,d5|WH,QU|科研教育,文娱商演,特种作业|-|oem
优必选|m1,d1|WH|工业制造,商用服务|-|oem
乐聚机器人|m1,d4|WH|科研教育,文娱商演|-|oem
星动纪元|m1,d2|WH|仓储物流,工业制造|-|oem
傅利叶智能|m1,d8|WH|医疗健康,科研教育|-|oem
开普勒机器人|m1|WH|工业制造|-|oem
众擎机器人|m1,d5|WH|文娱商演|-|oem
加速进化|m1,d4|WH|科研教育|-|oem
小鹏 IRON|m1|WH|工业制造|-|oem
小米 CyberOne|m1|WH|家庭,科研教育|-|oem
Tesla Optimus|m1|WH|工业制造,家庭|-|oem
Figure AI|m1,d1|WH|工业制造,仓储物流|-|oem
Agility Robotics|m1,d2|WH|仓储物流|-|oem
1X|m1,d6|WH|家庭|-|oem
NEURA Robotics|m1|WH|工业制造|-|oem
Boston Dynamics|m1,m3|WH,QU|特种作业,工业制造|-|oem
Apptronik|m1,d1|WH|工业制造|-|oem
银河通用|m2,d3|WA|商用服务,工业制造|-|oem
星海图|m2|WA|工业制造,科研教育|-|oem
自变量机器人|m2|WA|商用服务|-|oem
逐际动力|m2|WH,QU|科研教育|-|oem
松灵机器人|m2|WA|科研教育|-|oem
云深处|m3,d7|QU|特种作业,科研教育|-|oem
亿嘉和|m3,d7|QU|特种作业|-|oem
申昊科技|m3,d7|QU|特种作业|-|oem
中信重工开诚|m3,d7|QU,SP|特种作业,矿区港口|-|oem
ANYbotics|m3,d7|QU|特种作业|-|oem
节卡机器人|m9,d1|SP|工业制造|-|oem
遨博智能|m9,d1|SP|工业制造|-|oem
极智嘉|m9,d2|SP|仓储物流|-|oem
快仓智能|m9,d2|SP|仓储物流|-|oem
Physical Intelligence|m4|WH,HW,WA|工业制造,科研教育|-|model
Skild AI|m4|WH,HW|工业制造|-|model
NVIDIA GR00T|m4,s1|WH|科研教育,工业制造|-|model
Google DeepMind|m4|WH,HW|科研教育|-|model
上海 AI Lab|m4|WH|科研教育|-|model
NVIDIA Isaac|m5,s1|WH,HW,WA,QU|科研教育,工业制造|-|model
光轮智能|m5|WH,HW|科研教育,工业制造|-|model
群核科技|m5|WH,HW|科研教育|-|model
51WORLD|m5|WH,SP|科研教育,特种作业|-|model
海天瑞声|m5|WH,HW|科研教育|海天瑞声-首次覆盖报告|model
数据堂|m5|WH|科研教育|-|model
中科创达|m6|WH,HW,SP|工业制造,商用服务|中科创达-首次覆盖报告|model
东土科技|m6|WH|工业制造|-|model
顺丰科技|d2|WA,SP|仓储物流|-|ops
中国邮政|d2|WA,SP|仓储物流|-|ops
京东物流|d2|WA,SP|仓储物流|-|ops
九识智能|d2|SP|仓储物流|-|ops
新石器|d2|SP|仓储物流|-|ops
擎朗智能|d3|WA,SP|商用服务|-|ops
普渡科技|d3|WA|商用服务|-|ops
云迹科技|d3|WA|商用服务|-|ops
猎户星空|d3|WA|商用服务|-|ops
比亚迪|d1|WH,SP|工业制造|-|ops
富士康|d1|WH,SP|工业制造|-|ops
宁德时代产线|d1|WA|工业制造|-|ops
科沃斯|d6|SP|家庭|-|ops
追觅科技|d6|WH|家庭|-|ops
易控智驾|d9|SP|矿区港口|-|ops
希迪智驾|d9|SP|矿区港口|-|ops
西井科技|d9|SP|矿区港口|-|ops
阿里云|s1|WH,HW,WA,QU,SP|科研教育,工业制造|阿里巴巴-首次覆盖报告|infra
华为云|s1|WH,HW|工业制造,科研教育|-|infra
腾讯云|s1|WH,HW|科研教育|-|infra
火山引擎|s1|WH,HW|科研教育|-|infra
中国电子技术标准化研究院|s2|WH,HW|工业制造,科研教育|-|infra
赛西实验室|s2|WH,HW|工业制造|-|infra
TÜV 莱茵|s2|WH,HW|工业制造|-|infra
北京人形机器人创新中心|s3|WH,HW|科研教育,工业制造|-|infra
上海国地中心|s3|WH|科研教育|-|infra
广东具身智能创新中心|s3|WH,HW|工业制造|-|infra
"""

RAW['llm'] = """
英伟达|u1|FT,OW,MM|大模型训练,大模型推理|-|part
AMD|u1|FT,OW|大模型推理,大模型训练|-|part
博通|u1,u4|FT,OW|大模型训练,大模型推理|-|part
Google TPU|u1|FT,MM|大模型训练,大模型推理|-|part
AWS Trainium|u1|FT,OW|大模型训练,大模型推理|-|part
华为昇腾|u1|FT,OW|大模型训练,大模型推理|-|part
寒武纪|u1|FT,OW|大模型推理|-|part
海光信息|u1|FT,OW|大模型推理|-|part
沐曦|u1|FT,OW|大模型推理|-|part
壁仞科技|u1|FT|大模型训练|-|part
摩尔线程|u1|FT,OW|大模型训练|-|part
燧原科技|u1|OW|大模型推理|-|part
天数智芯|u1|FT,OW|大模型训练|-|part
景嘉微|u1|SM|端侧推理|-|part
Groq|u1|OW,MM|大模型推理|-|part
Cerebras|u1|FT|大模型训练|-|part
SK 海力士|u2|FT,OW,MM|大模型训练,大模型推理|-|part
三星电子|u2|FT,OW,MM|大模型训练,大模型推理|-|part
美光|u2|FT,OW|大模型训练|-|part
长鑫存储|u2|OW|大模型推理|-|part
台积电|u3|FT,OW,MM|大模型训练,大模型推理|-|part
中芯国际|u3|SM,OW|端侧推理|-|part
长电科技|u3|FT,OW|大模型训练|-|part
通富微电|u3|FT|大模型训练|-|part
中际旭创|u4|FT,OW|大模型训练,大模型推理|-|part
新易盛|u4|FT,OW|大模型训练,大模型推理|-|part
天孚通信|u4|FT,OW|大模型训练|-|part
Coherent|u4|FT|大模型训练|-|part
Lumentum|u4|FT|大模型训练|-|part
源杰科技|u4|FT,OW|大模型训练|-|part
光迅科技|u4|OW|大模型推理|-|part
戴尔|u5|FT,OW|大模型训练,大模型推理|-|part
超微电脑|u5|FT,OW|大模型训练|-|part
鸿海|u5|FT,OW|大模型训练|-|part
浪潮信息|u5|FT,OW|大模型训练,大模型推理|-|part
中科曙光|u5|FT,OW|大模型训练|-|part
联想|u5|OW|大模型推理|-|part
工业富联|u5|FT|大模型训练|-|part
英维克|u6|FT,OW|大模型训练,大模型推理|-|part
Vertiv|u6|FT,OW|大模型训练|-|part
施耐德电气|u6|FT,OW|大模型训练|-|part
伊顿|u6|FT|大模型训练|-|part
阳光电源|u6|FT,OW|大模型训练|-|part
华为数字能源|u6|FT,OW|大模型训练|-|part
海天瑞声|u7|FT,OW,MM|大模型训练|海天瑞声-首次覆盖报告|part
Scale AI|u7|FT,MM|大模型训练|-|part
Appen|u7|FT,OW|大模型训练|-|part
数据堂|u7|OW|大模型训练|-|part
OpenAI|m1|FT,MM|消费级应用,编程,科研与垂直|-|model
Anthropic|m1|FT,MM|编程,企业软件,科研与垂直|-|model
Google DeepMind|m1|FT,MM|消费级应用,科研与垂直|-|model
xAI|m1|FT,MM|消费级应用|-|model
Mistral AI|m1|FT,OW|企业软件,编程|-|model
Cohere|m1|FT|企业软件,知识库|-|model
AI21 Labs|m1|FT|企业软件|-|model
Meta Llama|m2|OW,SM|消费级应用,科研与垂直|-|model
DeepSeek|m2|OW,MM|编程,科研与垂直,消费级应用|-|model
阿里通义|m2|OW,SM,MM|企业软件,消费级应用|阿里巴巴-首次覆盖报告|model
月之暗面 Kimi|m2|OW,MM|消费级应用,编程|-|model
智谱 GLM|m2|OW,SM|企业软件,编程|-|model
MiniMax|m2|OW,MM|消费级应用,内容营销|-|model
腾讯混元|m2|OW,MM|企业软件,内容营销|-|model
小米 MiMo|m2|OW,SM|端侧推理,消费级应用|-|model
阶跃星辰|m2|OW,MM|消费级应用|-|model
百川智能|m2|OW|医疗健康,企业软件|-|model
零一万物|m2|OW,SM|企业软件|-|model
Harvey|m3|VT|科研与垂直|-|model
Hippocratic AI|m3|VT|医疗健康|-|model
BloombergGPT|m3|VT|科研与垂直|-|model
蚂蚁百灵|m3|VT,SM|金融,端侧推理|-|model
vLLM|m4|OW,MM|大模型推理,企业软件|-|tool
SGLang|m4|OW,MM|大模型推理,编程|-|tool
TensorRT-LLM|m4|FT,OW|大模型推理|-|tool
LMDeploy|m4|OW,SM|大模型推理,端侧推理|-|tool
Ollama|m4|SM,OW|端侧推理|-|tool
llama.cpp|m4|SM|端侧推理|-|tool
Triton|m5|FT,OW|大模型训练,大模型推理|-|tool
Apache TVM|m5|SM,OW|端侧推理|-|tool
XLA|m5|FT|大模型训练|-|tool
CANN|m5|FT,OW|大模型训练,大模型推理|-|tool
MXMACA|m5|OW|大模型推理|-|tool
ROCm|m5|FT,OW|大模型训练|-|tool
无问芯穹|m5,d1|FT,OW|大模型训练,大模型推理|-|tool
HAMi|m5|FT,OW|大模型训练,大模型推理|-|tool
OpenRouter|m6|FT,OW,MM|大模型推理|-|tool
Together AI|m6|OW,MM|大模型推理,大模型训练|-|tool
Fireworks AI|m6|OW,MM|大模型推理|-|tool
Pinecone|m6|VT|知识库|-|tool
Weaviate|m6|VT|知识库|-|tool
LangChain|m6|VT,MM|Agent 与工作流,知识库|-|tool
LlamaIndex|m6|VT|知识库|-|tool
LangGraph|m7|MM,VT|Agent 与工作流|-|tool
AutoGen|m7|MM|Agent 与工作流|-|tool
CrewAI|m7|MM|Agent 与工作流|-|tool
Dify|m7|VT,MM|Agent 与工作流,企业软件|-|tool
扣子 Coze|m7|VT,MM|Agent 与工作流,消费级应用|-|tool
Cursor|d1|FT,MM|编程|-|app
GitHub Copilot|d1|FT,MM|编程|-|app
Claude Code|d1|FT,MM|编程|-|app
通义灵码|d1|OW,VT|编程|-|app
CodeBuddy|d1|FT,OW|编程|-|app
Sierra|d2|FT,VT|客服与工单|-|app
Decagon|d2|FT|客服与工单|-|app
Intercom|d2|FT|客服与工单|-|app
智齿科技|d2|OW,VT|客服与工单|-|app
Glean|d3|FT,VT|知识库,企业软件|-|app
Notion AI|d3|FT|知识库,内容营销|-|app
Microsoft 365 Copilot|d7|FT|企业软件|-|app
Salesforce Agentforce|d7|FT,MM|企业软件,Agent 与工作流|-|app
ServiceNow|d7|FT|企业软件|-|app
钉钉 AI|d7|OW,VT|企业软件,Agent 与工作流|-|app
用友|d7|VT|企业软件|-|app
金蝶|d7|VT|企业软件|-|app
Jasper|d5|FT|内容营销|-|app
Copy.ai|d5|FT|内容营销|-|app
Midjourney|d5|MM|内容营销|-|app
可灵|d5|MM|内容营销|-|app
ChatGPT|d6|FT,MM|消费级应用,编程,内容营销|-|app
Claude|d6|FT,MM|消费级应用,编程|-|app
Gemini|d6|FT,MM|消费级应用|-|app
豆包|d6|OW,MM|消费级应用|-|app
腾讯元宝|d6|OW,MM|消费级应用|-|app
Perplexity|d6|FT,MM|消费级应用,科研与垂直|-|app
Character.AI|d6|VT|消费级应用|-|app
Elicit|d8|FT,VT|科研与垂直|-|app
Consensus|d8|FT|科研与垂直|-|app
Hugging Face|s1|OW,SM,MM|科研与垂直,大模型训练|-|infra
GitHub|s1|OW|编程|-|infra
AWS|s2|FT,OW,MM|大模型训练,大模型推理,公有云算力|-|infra
Microsoft Azure|s2|FT,MM|大模型训练,大模型推理|-|infra
Google Cloud|s2|FT,MM|大模型训练,大模型推理|-|infra
阿里云|s2|OW,MM|大模型训练,大模型推理|阿里巴巴-首次覆盖报告|infra
腾讯云|s2|OW,MM|大模型推理|-|infra
火山引擎|s2|OW,MM|大模型推理,公有云算力|-|infra
紫光股份|s2|FT,OW|公有云算力|紫光股份-三季报更新与评级|infra
中科创达|s2|SM,VT|端侧推理|中科创达-首次覆盖报告|infra
中国信通院|s3|FT,OW,MM|科研与垂直|-|infra
WAICO|s3|FT,OW|科研与垂直|-|infra
"""

RAW['infra'] = """
台积电|u1|TR,IN,FT|大模型训练,大模型推理|-|part
中芯国际|u1|ED,IN|端侧推理|-|part
长电科技|u2|TR,IN|大模型训练,大模型推理|-|part
通富微电|u2|TR,IN|大模型训练|-|part
SK 海力士|u3|TR,IN,MM|大模型训练,大模型推理|-|part
三星电子|u3|TR,IN|大模型训练,大模型推理|-|part
美光|u3|TR,IN|大模型训练|-|part
长鑫存储|u3|IN|大模型推理|-|part
兆易创新|u4|IN,ED|端侧推理,工业视觉|兆易创新-首次覆盖报告|part
江波龙|u4|IN,ED|端侧推理|-|part
佰维存储|u4|IN|大模型推理|-|part
Solidigm|u4|IN|大模型推理|-|part
源杰科技|u5|TR,IN|大模型训练,大模型推理|-|part
长光华芯|u5|TR,IN|大模型训练|-|part
Lumentum|u5|TR|大模型训练|-|part
Coherent|u5|TR,IN|大模型训练|-|part
世运电路|u6|TR,IN|大模型训练,大模型推理|世运电路-首次覆盖报告|part
沪电股份|u6|TR,IN|大模型训练|-|part
生益科技|u6|TR,IN|大模型训练|-|part
胜宏科技|u6|TR,IN|大模型训练|-|part
立讯精密|u6|TR,IN|大模型训练|-|part
安费诺|u6|TR,IN|大模型训练|-|part
英维克|u7|TR,IN|大模型训练,大模型推理|-|part
Vertiv|u7|TR,IN|大模型训练,大模型推理|-|part
施耐德电气|u7|TR,IN|大模型训练|-|part
伊顿|u7|TR|大模型训练|-|part
阳光电源|u7|TR,IN|大模型训练|-|part
华为数字能源|u7|TR,IN|大模型训练,大模型推理|-|part
金盘科技|u7|TR|大模型训练|-|part
英伟达|m1|TR,IN,FT,SI,ED|大模型训练,大模型推理,科研计算,自动驾驶训练|-|part
AMD|m1|TR,IN|大模型训练,大模型推理|-|part
博通|m1,m3|TR,IN|大模型训练,大模型推理|-|part
Marvell|m1,m3|TR,IN|大模型训练|-|part
Google TPU|m1|TR,IN|大模型训练,大模型推理|-|part
AWS Trainium|m1|TR,IN|大模型训练|-|part
华为昇腾|m1|TR,IN,FT|大模型训练,大模型推理|-|part
寒武纪|m1|TR,IN|大模型推理|-|part
海光信息|m1|TR,IN|大模型推理|-|part
沐曦|m1|TR,IN|大模型推理|-|part
壁仞科技|m1|TR|大模型训练|-|part
摩尔线程|m1|TR,IN|大模型训练|-|part
燧原科技|m1|IN|大模型推理|-|part
天数智芯|m1|TR,IN|大模型训练|-|part
景嘉微|m1|ED|端侧推理|-|part
Groq|m1|IN|大模型推理|-|part
Cerebras|m1|TR|大模型训练|-|part
地平线机器人|m1|ED,IN|端侧推理,自动驾驶训练|地平线机器人-首次覆盖报告|part
中际旭创|m2|TR,IN|大模型训练,大模型推理|-|part
新易盛|m2|TR,IN|大模型训练,大模型推理|-|part
天孚通信|m2|TR,IN|大模型训练|-|part
光迅科技|m2|IN|大模型推理|-|part
华工科技|m2|TR,IN|大模型训练|-|part
Arista|m3|TR,IN|大模型训练,大模型推理|-|part
思科|m3|TR,IN|大模型训练|-|part
锐捷网络|m3|TR,IN|大模型训练|-|part
紫光股份|m3,d2|TR,IN|公有云算力,大模型训练|紫光股份-三季报更新与评级|part
戴尔|m4|TR,IN|大模型训练,大模型推理|-|part
超微电脑|m4|TR,IN|大模型训练|-|part
鸿海|m4|TR,IN|大模型训练|-|part
浪潮信息|m4|TR,IN|大模型训练,大模型推理|-|part
中科曙光|m4,d1|TR,IN,SI|大模型训练,科研计算|-|part
联想|m4|IN|大模型推理|-|part
工业富联|m4|TR,IN|大模型训练|-|part
华为|m4,m8,d1|TR,IN,FT|大模型训练,大模型推理,公有云算力|-|part
中兴通讯|m4,m8,d1|TR,IN|大模型训练,大模型推理|-|part
曙光 scaleX|m5,d1|TR,SI|大模型训练,科研计算|-|part
英维克冷板|m5|TR,IN|大模型训练,大模型推理|-|part
申菱环境|m5|TR,IN|大模型训练|-|part
高澜股份|m5|TR,IN|大模型训练|-|part
vLLM|m6|IN,MM|大模型推理|-|soft
SGLang|m6|IN,MM|大模型推理|-|soft
TensorRT-LLM|m6|IN|大模型推理|-|soft
LMDeploy|m6|IN,ED|大模型推理,端侧推理|-|soft
Ollama|m6|ED|端侧推理|-|soft
Triton|m6|TR,IN|大模型训练,大模型推理|-|soft
Apache TVM|m6|ED,IN|端侧推理|-|soft
XLA|m6|TR|大模型训练|-|soft
CANN|m6|TR,IN|大模型训练,大模型推理|-|soft
MXMACA|m6|IN|大模型推理|-|soft
ROCm|m6|TR,IN|大模型训练|-|soft
无问芯穹|m7,d1|TR,IN|大模型训练,大模型推理,企业私有化|-|soft
HAMi|m7|TR,IN|大模型训练,大模型推理|-|soft
Kubeflow|m7|TR,IN|大模型训练|-|soft
Ray|m7|TR,IN|大模型训练|-|soft
Slurm|m7|TR,SI|大模型训练,科研计算|-|soft
Volcano|m7|TR|大模型训练|-|soft
中国联通|m7,d1|TR,IN|大模型训练,公有云算力|-|soft
中国移动|m7,d1|TR,IN|大模型训练,公有云算力|-|soft
中国电信|m7,d1|TR,IN|大模型训练,公有云算力|-|soft
中科创达|m6|ED,IN|端侧推理,工业视觉|中科创达-首次覆盖报告|soft
NVIDIA GB200 NVL72|m8|TR,IN|大模型训练,大模型推理|-|soft
华为 Atlas 950|m8,d1|TR,IN|大模型训练,大模型推理|-|soft
中兴超节点|m8,d1|TR,IN|大模型训练|-|soft
天数 IXL144|m8|TR,IN|大模型训练|-|soft
登峰 8000|m8,d1|TR,SI|大模型训练,科研计算|-|soft
阿里云|d2|TR,IN,FT|大模型训练,大模型推理,公有云算力|阿里巴巴-首次覆盖报告|svc
腾讯云|d2|TR,IN|大模型推理,公有云算力|-|svc
华为云|d2|TR,IN|大模型训练,公有云算力|-|svc
火山引擎|d2|IN,TR|大模型推理,公有云算力|-|svc
AWS|d2|TR,IN|大模型训练,大模型推理|-|svc
Microsoft Azure|d2|TR,IN|大模型训练,大模型推理|-|svc
Google Cloud|d2|TR,IN|大模型训练,大模型推理|-|svc
CoreWeave|d2|TR,IN|大模型训练,公有云算力|-|svc
Oracle Cloud|d2|TR,IN|大模型训练|-|svc
海天瑞声|d3|FT,MM|大模型训练,具身智能训练|海天瑞声-首次覆盖报告|svc
OpenAI|d3|TR,FT|大模型训练|-|svc
Anthropic|d3|TR,FT|大模型训练|-|svc
DeepSeek|d3|TR,FT|大模型训练|-|svc
月之暗面|d3|TR,FT|大模型训练|-|svc
字节跳动|d4|IN,TR|大模型推理,大模型训练|-|svc
百度|d4|IN,TR|大模型推理|-|svc
腾讯|d4|IN,TR|大模型推理|-|svc
阿里巴巴|d4|IN,TR|大模型推理,公有云算力|阿里巴巴-首次覆盖报告|svc
特斯拉|d3|TR,FT|自动驾驶训练|-|svc
比亚迪|d3|TR|自动驾驶训练|-|svc
小鹏汽车|d3|TR|自动驾驶训练|-|svc
智元机器人|d3|TR,FT|具身智能训练|-|svc
宇树科技|d3|TR,FT|具身智能训练|-|svc
银河通用|d3|TR,FT|具身智能训练|-|svc
宁德时代|d5|ED,IN|工业视觉|-|svc
国家电网|s1|TR,IN|大模型训练,大模型推理|-|svc
南方电网|s1|TR,IN|大模型训练|-|svc
三峡能源|s1|TR|大模型训练|-|svc
阳光电源|s1|TR,IN|大模型训练|-|svc
中国建筑|s2|TR,IN|大模型训练|-|svc
数据港|s2|TR,IN|大模型训练,大模型推理|-|svc
润泽科技|s2|TR,IN|大模型训练|-|svc
奥飞数据|s2|TR,IN|大模型推理|-|svc
光环新网|s2|TR,IN|大模型推理|-|svc
中国信通院|s3|TR,IN,SI|科研计算,大模型训练|-|svc
中国电子技术标准化研究院|s3|TR,IN|科研计算|-|svc
Uptime Institute|s3|TR,IN|科研计算|-|svc
"""

RAW['mobile'] = """
中国移动|u1|SOC,TOOL|即时通讯,移动支付,办公协作|-|infra
中国电信|u1|SOC,TOOL|即时通讯,办公协作|-|infra
中国联通|u1|SOC,TOOL|即时通讯,办公协作|-|infra
中国广电|u1|CON|内容消费|-|infra
高通|u2|SOC,CON,TOOL|即时通讯,内容消费,移动游戏|-|term
联发科|u2|SOC,CON|内容消费,移动游戏|-|term
苹果 A 系列|u2|TOOL,CON|办公协作,内容消费|-|term
华为海思|u2|TOOL,SOC|即时通讯,办公协作|-|term
紫光展锐|u2|SOC,TOOL|即时通讯|-|term
兆易创新|u2|TOOL|办公协作|兆易创新-首次覆盖报告|term
世运电路|u2|TOOL|办公协作|世运电路-首次覆盖报告|term
京东方|u2|CON,TOOL|内容消费,办公协作|-|term
舜宇光学|u2|CON|内容消费|-|term
地平线机器人|u2|TOOL,LIFE|本地生活,AI助手|地平线机器人-首次覆盖报告|term
虹软科技|u2|CON,TOOL|内容消费,AI助手|虹软科技-首次覆盖报告|term
苹果|u3|SOC,CON,COM,TOOL|即时通讯,内容消费,网络购物,移动支付,AI助手|-|term
华为终端|u3|SOC,CON,COM,TOOL|即时通讯,内容消费,网络购物,移动支付,AI助手|-|term
小米集团|u3|SOC,CON,COM,TOOL|即时通讯,内容消费,网络购物,AI助手|-|term
OPPO|u3|SOC,CON|即时通讯,内容消费|-|term
vivo|u3|SOC,CON|即时通讯,内容消费|-|term
荣耀|u3|SOC,CON|即时通讯,内容消费|-|term
三星电子|u3|SOC,CON|即时通讯,内容消费|-|term
传音控股|u3|SOC,CON|即时通讯,内容消费|-|term
iOS|u4|SOC,CON,COM,TOOL|即时通讯,内容消费,网络购物,AI助手|-|term
Android|u4|SOC,CON,COM,TOOL|即时通讯,内容消费,网络购物,AI助手|-|term
HarmonyOS NEXT|u4|SOC,CON,COM,TOOL|即时通讯,内容消费,网络购物,AI助手|-|term
中科创达|u4|TOOL,LIFE|办公协作,本地生活|中科创达-首次覆盖报告|term
微信小程序运行时|u4|COM,LIFE,TOOL|网络购物,本地生活,办公协作|-|term
阿里云|u5|COM,TOOL|网络购物,办公协作|阿里巴巴-首次覆盖报告|infra
腾讯云|u5|SOC,TOOL|即时通讯,办公协作|-|infra
华为云|u5|TOOL|办公协作|-|infra
火山引擎|u5|CON,COM|内容消费,网络购物|-|infra
百度智能云|u5|TOOL,CON|AI助手,内容消费|-|infra
紫光股份|u5|TOOL|办公协作|紫光股份-三季报更新与评级|infra
网宿科技|u5|CON,COM|内容消费,网络购物|-|infra
金山云|u5|TOOL|办公协作|-|infra
海天瑞声|u6|TOOL|AI助手|海天瑞声-首次覆盖报告|support
数据堂|u6|TOOL|AI助手|-|support
App Store|m1|CON,COM,TOOL|内容消费,网络购物,移动游戏|-|term
Google Play|m1|CON,COM,TOOL|内容消费,网络购物,移动游戏|-|term
华为应用市场|m1|CON,COM,TOOL|内容消费,网络购物,移动游戏|-|term
小米应用商店|m1|CON,COM,TOOL|内容消费,网络购物,移动游戏|-|term
腾讯应用宝|m1|CON,TOOL|内容消费,移动游戏|-|term
微信|m2|SOC,COM,LIFE,TOOL|即时通讯,移动支付,本地生活,网络购物,办公协作,AI助手|-|platform
QQ|m2|SOC,CON|即时通讯,内容消费,移动游戏|-|platform
微博|m2|SOC,CON|即时通讯,内容消费|-|platform
钉钉|m2|SOC,TOOL|即时通讯,办公协作|阿里巴巴-首次覆盖报告|platform
企业微信|m2|SOC,TOOL|即时通讯,办公协作|-|platform
飞书|m2|SOC,TOOL|即时通讯,办公协作|-|platform
抖音|m3|CON,COM,LIFE|内容消费,网络购物,本地生活|-|platform
快手|m3|CON,COM|内容消费,网络购物|-|platform
微信视频号|m3|CON,COM|内容消费,网络购物|-|platform
小红书|m3|CON,COM,LIFE|内容消费,网络购物,本地生活|-|platform
哔哩哔哩|m3|CON,COM|内容消费,网络购物,移动游戏|-|platform
今日头条|m3|CON|内容消费|-|platform
阅文集团|m3|CON|内容消费|阅文集团-首次覆盖报告|vertical
番茄小说|m3|CON|内容消费|-|vertical
爱奇艺|m3|CON|内容消费|-|vertical
腾讯视频|m3|CON|内容消费|-|vertical
喜马拉雅|m3|CON|内容消费|-|vertical
知乎|m3|CON,TOOL|内容消费,AI助手|-|vertical
淘宝|m4|COM|网络购物|阿里巴巴-首次覆盖报告|platform
天猫|m4|COM|网络购物|-|platform
京东|m4|COM,LIFE|网络购物,本地生活|-|platform
拼多多|m4|COM|网络购物|-|platform
抖音商城|m4|COM|网络购物|-|platform
唯品会|m4|COM|网络购物|-|vertical
名创优品|m4|COM,LIFE|网络购物,本地生活|名创优品-首次覆盖报告|vertical
永辉超市|m4|COM,LIFE|网络购物,本地生活|永辉超市-首次覆盖报告|vertical
万辰集团|m4|COM|网络购物|万辰集团-首次覆盖报告|vertical
东鹏饮料|m4|COM|网络购物|东鹏饮料-首次覆盖报告|vertical
天味食品|m4|COM|网络购物|天味食品-首次覆盖报告|vertical
潮宏基|m4|COM|网络购物|潮宏基-首次覆盖报告|vertical
菜百股份|m4|COM|网络购物|菜百股份-首次覆盖报告|vertical
曼卡龙|m4|COM|网络购物|曼卡龙-首次覆盖报告|vertical
美团|m5|LIFE,COM|本地生活,网络购物|-|platform
大众点评|m5|LIFE|本地生活|-|platform
饿了么|m5|LIFE|本地生活|阿里巴巴-首次覆盖报告|platform
滴滴出行|m5|LIFE|本地生活|-|vertical
高德地图|m5|LIFE,TOOL|本地生活,AI助手|阿里巴巴-首次覆盖报告|vertical
百度地图|m5|LIFE,TOOL|本地生活,AI助手|-|vertical
携程|m5|LIFE|本地生活|-|vertical
贝壳找房|m5|LIFE|本地生活|-|vertical
哈啰出行|m5|LIFE|本地生活|-|vertical
腾讯游戏|m6|CON|移动游戏|-|vertical
网易游戏|m6|CON|移动游戏|-|vertical
米哈游|m6|CON|移动游戏|-|vertical
巨人网络|m6|CON|移动游戏|巨人网络-首次覆盖报告|vertical
三七互娱|m6|CON|移动游戏|-|vertical
A股游戏板块|m6|CON|移动游戏|A股游戏板块-同业对比分析|vertical
腾讯广告|m7|CON,COM|内容消费,网络购物|-|platform
巨量引擎|m7|CON,COM|内容消费,网络购物|-|platform
阿里妈妈|m7|COM|网络购物|阿里巴巴-首次覆盖报告|platform
百度营销|m7|CON,TOOL|内容消费,AI助手|-|platform
分众传媒|m7|CON,COM|内容消费,网络购物|-|support
支付宝|m8|COM,LIFE,TOOL|移动支付,网络购物,本地生活,办公协作|阿里巴巴-首次覆盖报告|platform
微信支付|m8|SOC,LIFE,TOOL|移动支付,即时通讯,本地生活|-|platform
中国银联|m8|TOOL,LIFE|移动支付,本地生活|-|support
网联清算|m8|TOOL|移动支付|-|support
拉卡拉|m8|LIFE,TOOL|移动支付,本地生活|-|support
数字人民币|m8|TOOL,LIFE|移动支付,本地生活|-|support
豆包|m9|TOOL,CON|AI助手,内容消费|-|platform
腾讯元宝|m9|TOOL,SOC|AI助手,即时通讯|-|platform
Kimi|m9|TOOL|AI助手,办公协作|-|vertical
DeepSeek App|m9|TOOL|AI助手,办公协作|-|vertical
文心一言|m9|TOOL|AI助手|-|platform
通义千问|m9|TOOL,COM|AI助手,网络购物|阿里巴巴-首次覆盖报告|platform
夸克|m9|TOOL,CON|AI助手,内容消费,办公协作|-|platform
纳米AI搜索|m9|TOOL|AI助手|-|vertical
即时零售|d1|COM,LIFE|网络购物,本地生活|-|vertical
生鲜电商|d1|COM,LIFE|网络购物,本地生活|-|vertical
直播电商|d2|COM,CON|网络购物,内容消费|-|vertical
短剧平台|d2|CON|内容消费|-|vertical
移动云游戏|d3|CON|移动游戏|-|vertical
游戏出海|d3|CON|移动游戏|-|vertical
有赞|d4|COM,TOOL|网络购物,办公协作|-|support
微盟|d4|COM,TOOL|网络购物,办公协作|-|support
商户SaaS|d4|LIFE,TOOL|本地生活,办公协作|-|support
TikTok|d5|CON,COM|内容消费,网络购物|-|platform
SHEIN|d5|COM|网络购物|-|vertical
Temu|d5|COM|网络购物|-|vertical
支付宝国际|d5|TOOL,LIFE|移动支付,本地生活|阿里巴巴-首次覆盖报告|support
银发与下沉服务|d6|CON,COM,LIFE|内容消费,网络购物,本地生活|-|vertical
适老化改造|d6|TOOL,LIFE|办公协作,本地生活|-|support
QuestMobile|s1|TOOL,CON|办公协作,内容消费|-|support
月狐数据|s1|TOOL|办公协作|-|support
清科控股|s1|TOOL|办公协作|清科控股-首次覆盖报告|support
中国信通院|s2|TOOL|办公协作|-|support
中国互联网协会|s2|TOOL|办公协作|-|support
国家网信办|s2|TOOL|办公协作|-|support
360|s3|TOOL|办公协作,AI助手|-|support
奇安信|s3|TOOL|办公协作|-|support
蚂蚁集团|s3|TOOL,LIFE|移动支付,本地生活|-|support
"""

RAW['space'] = """
蓝箭航天|m1,u1|LC,LV|宽带接入,国防与政府|-|rocket
天兵科技|m1,u1|LC,LV|宽带接入,国防与政府|-|rocket
星际荣耀|m1,u1|LV|国防与政府,应急通信|-|rocket
星河动力|m1,u1|LV,LO|遥感监测,国防与政府|-|rocket
中科宇航|m1,u1|LV,LC|遥感监测,国防与政府|-|rocket
东方空间|m1,u1|LV,LC|宽带接入|-|rocket
深蓝航天|m1,u1|LV|国防与政府|-|rocket
九州云箭|u1|LV|宽带接入|-|supplier
航天六院|u1|LV,LC|宽带接入|-|soe
航天环宇|u2|LV,LC|宽带接入|-|supplier
铂力特|u2|LV|宽带接入|-|supplier
光威复材|u2|LV|宽带接入|-|supplier
中简科技|u2|LV|宽带接入|-|supplier
西部超导|u2|LV|国防与政府|-|supplier
钢研高纳|u2|LV|国防与政府|-|supplier
抚顺特钢|u2|LV|国防与政府|-|supplier
楚江新材|u2|LV|国防与政府|-|supplier
航天晨光|u2|LV|国防与政府|-|soe
铖昌科技|u3|LC,LO|宽带接入,遥感监测|-|supplier
臻镭科技|u3|LC|宽带接入,手机直连|-|supplier
振芯科技|u3|NAV,LC|导航增强,国防与政府|-|supplier
复旦微电|u3|LC|宽带接入|-|supplier
紫光国微|u3|LC|国防与政府|-|supplier
国光电气|u3|LC|国防与政府|-|supplier
振华风光|u3|LC|国防与政府|-|supplier
天箭科技|u3|LC|国防与政府|-|supplier
雷科防务|u3,u5|LO,LC|遥感监测,国防与政府|-|supplier
有研新材|u3|LC|宽带接入|-|supplier
中电科13所|u3|LC|国防与政府|-|soe
中电科55所|u3|LC|国防与政府|-|soe
火炬电子|u8|LC|国防与政府|-|supplier
宏达电子|u8|LC|国防与政府|-|supplier
鸿远电子|u8|LC|国防与政府|-|supplier
航天电器|u8|LV,LC|宽带接入|-|supplier
中国卫星|m2,u4|LO,LC|遥感监测,宽带接入|-|soe
银河航天|m2,u4|LC|宽带接入,手机直连|-|satellite
微纳星空|m2,u4|LO,LC|遥感监测|-|satellite
长光卫星|m2,u6|LO|遥感监测|-|satellite
时空道宇|m2,m7|LC|卫星物联网,手机直连|-|satellite
国电高科|m7,m2|LC|卫星物联网|-|satellite
天仪研究院|m2|LO|遥感监测|-|satellite
九天微星|m2|LC|卫星物联网|-|satellite
上海沪工|m2,u6|LC,LO|宽带接入,遥感监测|-|supplier
航天科技集团|m1,m2|LC,LV,DEEP|宽带接入,国防与政府|-|soe
中国航天科工|m1,m2|LV,LC|国防与政府|-|soe
中国星网|m6,m3|LC|宽带接入,手机直连|-|soe
垣信卫星|m6,m3|LC|宽带接入,手机直连|-|soe
航天东方红|m2|LO,LC|遥感监测|-|soe
中科院微小卫星|m2|LO|遥感监测|-|soe
魔方卫星|m2|LO|遥感监测|-|satellite
零重空间|m2|LO|遥感监测|-|satellite
上海瀚讯|u5,m3|LC|宽带接入,手机直连|-|supplier
航天电子|u5,u4|LC,LO|国防与政府,遥感监测|-|soe
盟升电子|u6,u7|NAV,LC|导航增强,手机直连|-|supplier
盛路通信|u7|LC|宽带接入|-|supplier
通宇通讯|u7|LC|宽带接入|-|supplier
硕贝德|u7|LC|手机直连|-|supplier
信维通信|u7,u3|LC|手机直连,宽带接入|-|supplier
三维通信|u7|LC|宽带接入|-|supplier
星移联信|u5,m3|LC|手机直连|-|satellite
海格通信|u7,u6|LC,NAV|应急通信,导航增强|-|supplier
华力创通|u7,u6|LC,NAV|手机直连,应急通信|-|supplier
北斗星通|d2,u7|NAV|导航增强|-|supplier
华测导航|d2,u7|NAV|导航增强|-|supplier
中海达|d2,u7|NAV|导航增强|-|supplier
合众思壮|d2,u7|NAV|导航增强|-|supplier
移远通信|u7,u3|LC|卫星物联网,手机直连|-|supplier
广和通|u7,u3|LC|卫星物联网|-|supplier
星网宇达|d2,u7|NAV|导航增强|-|supplier
中国卫通|m5,m3|GEO,LC|宽带接入,应急通信|-|soe
震有科技|m3|LC|宽带接入,手机直连|-|supplier
中电科54所|m3,m5|LC|国防与政府|-|soe
天奥电子|m3,m5|NAV|导航增强|-|soe
航天测控|m5|LC|宽带接入|-|soe
航天驭星|m3,m5|LC|宽带接入|-|app
海南商业发射场|m4|LV|国防与政府|-|soe
东方航天港|m4|LV|国防与政府|-|soe
中国移动|m6|LC|手机直连,宽带接入|-|operator
中国电信|m6|GEO,LC|手机直连,应急通信|-|operator
中国联通|m6|LC|手机直连,宽带接入|-|operator
亚太卫星|m5,m6|GEO|宽带接入,海事与航空|-|soe
亚洲卫星|m5,m6|GEO|海事与航空|-|soe
中科星图|d1,d3|LO|遥感监测,国防与政府|-|app
航天宏图|d1|LO|遥感监测|-|app
超图软件|d1,d3|LO|遥感监测|-|app
二十一世纪空间技术|d1|LO|遥感监测|-|app
四维图新|d2,d3|NAV|导航增强|-|app
中科天塔|d3|LC|应急通信,卫星物联网|-|app
华为|u7,u3,d3|LC,NAV|手机直连,应急通信|-|supplier
中兴通讯|u3,m3|LC|手机直连,宽带接入|-|supplier
信科移动|u3,m3|LC|手机直连|-|supplier
SpaceX|m1,m6|LC,LV|宽带接入,手机直连|-|rocket
Amazon Kuiper|m6,m2|LC|宽带接入|-|operator
Eutelsat OneWeb|m6|LC|宽带接入,海事与航空|-|operator
AST SpaceMobile|m6,m2|LC|手机直连|-|operator
Rocket Lab|m1|LV|国防与政府|-|rocket
Blue Origin|m1|LV,LC|宽带接入|-|rocket
ULA|m1|LV|国防与政府|-|rocket
Arianespace|m1|LV|国防与政府|-|rocket
Planet Labs|d1,m2|LO|遥感监测|-|app
Maxar|d1|LO|遥感监测|-|app
ICEYE|d1|LO|遥感监测|-|app
Iridium|m6,m7|LC|卫星物联网,海事与航空|-|operator
Viasat|m6|GEO|海事与航空,宽带接入|-|operator
SES|m6|GEO|宽带接入|-|operator
Intelsat|m6|GEO|宽带接入|-|operator
Telesat|m6|LC|宽带接入|-|operator
Axiom Space|d4|DEEP|国防与政府|-|app
Astroscale|d4|DEEP|国防与政府|-|app
Varda Space|d4|DEEP|国防与政府|-|app
Sierra Space|d4|DEEP|国防与政府|-|app
Northrop Grumman|d4|DEEP|国防与政府|-|soe
航天软件|s1|LC|宽带接入|-|supplier
康拓红外|s1|LC|国防与政府|-|supplier
思科瑞|s1|LC|国防与政府|-|supplier
西测测试|s1|LC|国防与政府|-|supplier
苏试试验|s1|LC|国防与政府|-|supplier
航天发展|s2|LC|国防与政府|-|soe
航天投资|s2|LC|宽带接入|-|soe
"""

RAW['device'] = """
恒玄科技|u1|WEAR,EYE|影音娱乐,办公与学习|-|chip
乐鑫科技|u1|HOME,TOY|家庭清洁,办公与学习|-|chip
瑞芯微|u1|EYE,HOME|影音娱乐,办公与学习|-|chip
晶晨股份|u1|HOME,WEAR|影音娱乐|-|chip
全志科技|u1|HOME,TOY|影音娱乐|-|chip
炬芯科技|u1|WEAR|影音娱乐|-|chip
中科蓝讯|u1|WEAR|影音娱乐|-|chip
泰凌微|u1|HOME|家庭清洁|-|chip
兆易创新|u1|WEAR,HOME|影音娱乐|兆易创新-首次覆盖报告|chip
高通|u1|EYE,WEAR|影音娱乐,办公与学习|-|chip
联发科|u1|WEAR,HOME|影音娱乐|-|chip
星宸科技|u2|HOME|家庭清洁,宠物|-|chip
北京君正|u2|WEAR,HOME|影音娱乐|-|chip
富瀚微|u2|HOME|家庭清洁|-|chip
安霸|u2|IMAGE,EYE|运动与户外|-|chip
虹软科技|u2,m7|IMAGE,HOME|影音娱乐|虹软科技-首次覆盖报告|odms
舜宇光学|u3|IMAGE,EYE|运动与户外|-|chip
欧菲光|u3|IMAGE,HOME|运动与户外|-|chip
联创电子|u3|IMAGE,EYE|运动与户外|-|chip
水晶光电|u3|EYE,IMAGE|影音娱乐|-|chip
蓝特光学|u3|EYE|影音娱乐|-|chip
至格科技|u3|EYE|影音娱乐|-|chip
JBD 镭昱|u3|EYE|影音娱乐|-|chip
京东方|u3|WEAR,HOME|影音娱乐|-|chip
维信诺|u3|WEAR|影音娱乐|-|chip
三安光电|u3|EYE|影音娱乐|-|chip
韦尔股份|u4|IMAGE,HOME|运动与户外,家庭清洁|-|chip
思特威|u4|HOME,IMAGE|家庭清洁|-|chip
汇顶科技|u4|WEAR|健康监测|-|chip
士兰微|u4|HOME|家庭清洁|-|chip
华工科技|u4|CLEAN|家庭清洁|-|chip
禾赛科技|u4|CLEAN|家庭清洁|-|chip
速腾聚创|u4|CLEAN|家庭清洁|-|chip
歌尔股份|u5,m6|WEAR,EYE|影音娱乐|-|odms
瑞声科技|u5|WEAR|影音娱乐|-|chip
国光电器|u5|WEAR|影音娱乐|-|chip
共达电声|u5|WEAR|影音娱乐|-|chip
亿纬锂能|u6|WEAR,CLEAN|健康监测|-|chip
欣旺达|u6|WEAR,CLEAN|影音娱乐|-|chip
珠海冠宇|u6|WEAR|影音娱乐|-|chip
德赛电池|u6|WEAR|影音娱乐|-|chip
紫建电子|u6|WEAR|影音娱乐|-|chip
南芯科技|u6|WEAR,HOME|影音娱乐|-|chip
蓝思科技|u7|EYE,WEAR|影音娱乐|-|odms
长盈精密|u7|WEAR,HOME|影音娱乐|-|odms
领益智造|u7|WEAR,HOME|影音娱乐|-|odms
科森科技|u7|WEAR|影音娱乐|-|odms
精研科技|u7|WEAR|影音娱乐|-|odms
立讯精密|u7,m6|WEAR,EYE|影音娱乐|-|odms
世运电路|u8|CLEAN,WEAR|家庭清洁|世运电路-首次覆盖报告|chip
鹏鼎控股|u8|WEAR,EYE|影音娱乐|-|chip
东山精密|u8|WEAR|影音娱乐|-|chip
风华高科|u8|WEAR,HOME|影音娱乐|-|chip
三环集团|u8|WEAR|影音娱乐|-|chip
顺络电子|u8|WEAR,HOME|影音娱乐|-|chip
移远通信|u9|HOME,TOY|家庭清洁,宠物|-|chip
广和通|u9|HOME,TOY|家庭清洁|-|chip
美格智能|u9|HOME|家庭清洁|-|chip
电连技术|u9|WEAR|影音娱乐|-|chip
意华股份|u9|HOME|家庭清洁|-|chip
石头科技|m1|CLEAN|家庭清洁|-|brand
科沃斯|m1|CLEAN|家庭清洁|-|brand
追觅科技|m1|CLEAN|家庭清洁|-|brand
云鲸智能|m1|CLEAN|家庭清洁|-|brand
添可|m1|CLEAN|家庭清洁|-|brand
莱克电气|m1|CLEAN|家庭清洁|-|brand
德尔玛|m1|CLEAN|家庭清洁|-|brand
iRobot|m1|CLEAN|家庭清洁|-|brand
杉川机器人|m1,m6|CLEAN|家庭清洁|-|odms
小米|m1,m2,m4|CLEAN,WEAR,HOME|家庭清洁,影音娱乐,健康监测,车载与出行|-|brand
华为|m2,m5|WEAR,EYE|健康监测,影音娱乐,车载与出行|-|brand
苹果|m2|WEAR|健康监测,影音娱乐|-|brand
三星电子|m2|WEAR|健康监测|-|brand
佳明 Garmin|m2|WEAR|运动与户外,健康监测|-|brand
华米科技|m2|WEAR|健康监测|-|brand
漫步者|m2|WEAR|影音娱乐|-|brand
韶音科技|m2|WEAR|运动与户外|-|brand
OPPO|m2|WEAR|健康监测|-|brand
vivo|m2|WEAR|健康监测|-|brand
小天才|m2|WEAR|老人与儿童|-|brand
安克创新|m2,m4|WEAR,HOME|办公与学习,影音娱乐|-|brand
影石创新|m3|IMAGE|运动与户外|-|brand
大疆|m3|IMAGE|运动与户外,车载与出行|-|brand
GoPro|m3|IMAGE|运动与户外|-|brand
萤石网络|m3,m4|HOME,IMAGE|宠物,家庭清洁|-|brand
小蚁科技|m3,m4|HOME|家庭清洁|-|brand
70迈|m3|IMAGE|车载与出行|-|brand
盯盯拍|m3|IMAGE|车载与出行|-|brand
绿联科技|m4|HOME|办公与学习|-|brand
鹿客科技|m4|HOME|家庭清洁|-|brand
凯迪仕|m4|HOME|家庭清洁|-|brand
德施曼|m4|HOME|家庭清洁|-|brand
极米科技|m4|HOME|影音娱乐|-|brand
坚果投影|m4|HOME|影音娱乐|-|brand
当贝|m4|HOME|影音娱乐|-|brand
云米科技|m4|HOME|家庭清洁|-|brand
小佩宠物|m4|HOME|宠物|-|brand
霍曼科技|m4|HOME|宠物|-|brand
CATLINK|m4|HOME|宠物|-|brand
泡泡玛特|m4|TOY|老人与儿童,影音娱乐|-|brand
字节跳动|m4|TOY|老人与儿童,影音娱乐|-|brand
奥飞娱乐|m4|TOY|老人与儿童|-|brand
实丰文化|m4|TOY|老人与儿童|-|brand
Meta|m5|EYE|影音娱乐,办公与学习|-|brand
雷鸟创新 RayNeo|m5|EYE|影音娱乐|-|brand
Rokid|m5|EYE|办公与学习,影音娱乐|-|brand
XREAL|m5|EYE|影音娱乐|-|brand
Viture|m5|EYE|影音娱乐|-|brand
李未可|m5|EYE|影音娱乐|-|brand
闪极|m5|EYE|影音娱乐|-|brand
亮亮视野|m5|EYE|办公与学习|-|brand
阿里巴巴|m5|EYE|办公与学习|-|brand
Snap|m5|EYE|影音娱乐|-|brand
跃然创新|m5,m4|TOY|老人与儿童|-|brand
华勤技术|m6|HOME,WEAR|家庭清洁|-|odms
龙旗科技|m6|WEAR,HOME|影音娱乐|-|odms
闻泰科技|m6|WEAR|影音娱乐|-|odms
光弘科技|m6|HOME|家庭清洁|-|odms
深科技|m6|WEAR|影音娱乐|-|odms
卓翼科技|m6|HOME|家庭清洁|-|odms
比亚迪电子|m6|WEAR,HOME|影音娱乐|-|odms
中科创达|m7|WEAR,HOME|影音娱乐|中科创达-首次覆盖报告|odms
涂鸦智能|m7,m4|HOME|家庭清洁|-|odms
翱捷科技|m7,u1|HOME|家庭清洁|-|chip
亚马逊|d1|HOME,WEAR|办公与学习|-|plat
京东|d1|HOME,WEAR|家庭清洁|-|plat
天猫|d1|HOME,WEAR|家庭清洁|-|plat
拼多多|d1|HOME|家庭清洁|-|plat
抖音电商|d1|HOME,WEAR|影音娱乐|-|plat
速卖通|d1|HOME|办公与学习|-|plat
Temu|d1|HOME|家庭清洁|-|plat
苏宁易购|d2|HOME,WEAR|家庭清洁|-|plat
顺电|d2|HOME|家庭清洁|-|plat
中国移动|d2|WEAR|健康监测|-|plat
中国电信|d2|WEAR|健康监测|-|plat
山姆会员店|d2|HOME|家庭清洁|-|plat
Best Buy|d2|HOME,WEAR|影音娱乐|-|plat
Apple App Store|d3|WEAR|影音娱乐|-|supp
腾讯音乐|d3|WEAR|影音娱乐|-|supp
网易云音乐|d3|WEAR|影音娱乐|-|supp
喜马拉雅|d3|WEAR|影音娱乐|-|supp
华为运动健康|d3|WEAR|健康监测|-|supp
品胜|d4|WEAR,HOME|影音娱乐|-|supp
倍思|d4|WEAR|影音娱乐|-|supp
米家生态链|d4|HOME|家庭清洁|-|supp
中国质量认证中心|s1|HOME,WEAR|家庭清洁|-|supp
SGS|s1|HOME|家庭清洁|-|supp
TÜV 莱茵|s1|HOME,EYE|影音娱乐|-|supp
中国信通院|s1|WEAR,HOME|健康监测|-|supp
连接标准联盟 CSA|s2|HOME|家庭清洁|-|supp
蓝牙技术联盟|s2|WEAR|影音娱乐|-|supp
星闪联盟|s2|WEAR,HOME|影音娱乐|-|supp
京东物流|s3|HOME|家庭清洁|-|supp
顺丰|s3|HOME|家庭清洁|-|supp
菜鸟|s3|HOME|家庭清洁|-|supp
"""

# ---------- 各行业配置 ----------
SITES = {
'embodied': {
  'slug':'embodied-ai-landscape','title':'具身智能产业研究','en':'Embodied AI Research',
  'brand':'具身智能产业研究','doc':'具身智能行业观察笔记','docfile':'具身智能行业观察笔记.html',
  'tagline':'一份个人整理的行业笔记',
  'intro':'从丝杠谐波到人形整机，把这条产业链拆成 @@SEGN@@ 个环节、@@TOTAL@@ 家企业。<b>供应链图谱含全链条</b>；<b>本体形态</b>、<b>应用场景</b>、<b>玩家模式</b>三个视图只收录整机、模型软件与场景运营方。点击带绿点的公司名，直达调研报告。',
  'seg':'23','tech':'5','scene':'8',
  'tabs':['供应链图谱','按本体形态','按应用场景','按玩家模式'],
  'scope2':'口径：仅含<b>整机厂商、具身模型与软件、场景运营方</b>。上游减速器、丝杠、电机、传感器等零部件与支撑层不参与此视图——同一颗谐波减速器会同时装进人形、轮式和四足本体，按形态归类会失真。一家企业可横跨多列，取决于其产品线覆盖。',
  'scope3':'口径：仅含<b>整机厂商、具身模型与软件、场景运营方</b>。零部件企业不按场景归类——同一家电机厂会同时服务工业、物流与家庭。一家企业可覆盖多个场景，标记数字即为其跨环节数量。',
  'scope4':'口径：行是<b>玩家模式</b>（卖什么、担什么责），列是<b>本体形态</b>。同一家企业可在同一行内横跨多列。<b>形态拆五列，拆的不是等级、是物理载体</b>：双足赌通用场景，轮式与专用机赌成本效率，两者客户与账期完全不同。零部件与供应商不参与模式矩阵，理由见页脚。',
  'note4':'<b>两个值得注意的空格</b>：零部件供应商 × 家庭场景基本为空（家庭对价格与可靠性最苛刻，零件厂不直接面对终端）；场景运营方 × 人形双足仍稀薄（真正在工厂常态化跑的，目前多为轮式或专用机）。',
  'about':'企业按“主营业环节”归类，横跨多个环节的公司（如宇树、英伟达、华为）会在多处出现，用“多环节”标记。本体形态按“该企业主力产品载体”标注；应用场景按“已落地的场景”标注，同样可跨多个场景。<b>“按本体形态”“按应用场景”“按玩家模式”三个视图只收录整机、模型软件与场景运营方</b>——上游零部件与支撑层不参与，因为它们一套产品同时服务全部形态与场景。归类为编辑判断，非官方口径。',
  'layers':[('01','上游','减速器 · 丝杠 · 电机 · 传感器 · 灵巧手 · 芯片'),('02','中游','整机 · 本体 · 具身大模型 · 仿真数据'),('03','下游','工业 · 物流 · 商用 · 家庭 · 特种')],
  'supportdesc':'云算力 · 测试认证 · 创新中心',
  'SEG':{
   'u1':['上游','谐波 / RV 减速器'],'u2':['上游','行星滚柱丝杠'],'u3':['上游','电机与执行器'],
   'u4':['上游','力 / 触觉传感器'],'u5':['上游','3D 视觉与惯导'],'u6':['上游','灵巧手'],
   'u7':['上游','端侧 AI 芯片'],'u8':['上游','电池与轻量化'],'u9':['上游','光芯片 / PCB'],
   'm1':['中游','人形整机'],'m2':['中游','轮式双臂本体'],'m3':['中游','四足与特种本体'],
   'm4':['中游','具身大模型'],'m5':['中游','仿真 · 数据 · 工具链'],
   'm6':['中游','控制器与 OS'],'m9':['中游','专用 / 协作机器人'],
   'd1':['下游','工业制造'],'d2':['下游','仓储物流'],'d3':['下游','商用服务'],
   'd4':['下游','科研教育'],'d5':['下游','文娱商演'],'d6':['下游','家庭'],
   'd7':['下游','特种作业'],'d8':['下游','医疗健康'],'d9':['下游','矿区港口'],
   's1':['支撑层','云与训练算力'],'s2':['支撑层','测试认证与标准'],'s3':['支撑层','场景开放与创新中心']
  },
  'SUPPORT':['s1','s2','s3'],
  'APP_SEGS':['m1','m2','m3','m4','m5','m6','m9','d1','d2','d3','d4','d5','d6','d7','d8','d9'],
  'TECH':[['WH','人形双足','赌通用场景 · 最难'],['HW','人形轮式','上半身人形 · 稳定优先'],['WA','轮式双臂','不为像人 · 为干活'],['QU','四足','巡检安防 · 商业化较早'],['SP','专用机器人','分拣搬运 · 已在赚钱']],
  'TSHORT':{'WH':'人形双足','HW':'人形轮式','WA':'轮式双臂','QU':'四足','SP':'专用'},
  'SCENE':[['工业制造','真需求，但还在验证期'],['仓储物流','目前最像真生意'],['商用服务','酒店零售，任务清晰'],['科研教育','当前最大出货去向'],['文娱商演','有现金流，天花板低'],['家庭','泛化与安全未到位'],['特种作业','巡检安防，四足先行'],['医疗健康','高价值但小众']],
  'MODES':[['oem','整机厂商','卖本体 · 担交付责任','#1b4a75'],['part','零部件供应商','卖零件 · 不面对终端','#8a6416'],['model','模型与软件','卖智能 · 按授权或项目','#5f6b7a'],['ops','场景运营方','卖结果 · 按工时或运力','#a8271f'],['infra','基础设施与支撑','卖算力 · 认证与场景','#2f6f5e']],
  'BLANKS':[],
},
'llm': {
  'slug':'llm-landscape','title':'大语言模型产业研究','en':'LLM Research',
  'brand':'大语言模型产业研究','doc':'大语言模型行业观察笔记','docfile':'大语言模型行业观察笔记.html',
  'tagline':'一份个人整理的行业笔记',
  'intro':'从 HBM 到 Agent 应用，把这条产业链拆成 @@SEGN@@ 个环节、@@TOTAL@@ 家企业。<b>供应链图谱含全链条</b>；<b>模型层级</b>、<b>应用场景</b>、<b>玩家模式</b>三个视图只收录模型、工具与应用厂商。点击带绿点的公司名，直达调研报告。',
  'seg':'23','tech':'5','scene':'8',
  'tabs':['供应链图谱','按模型层级','按应用场景','按玩家模式'],
  'scope2':'口径：仅含<b>基础模型、推理框架与中间层、应用厂商</b>。上游芯片、HBM、光模块、服务器与云基础设施不参与此视图——同一张 GPU 既跑训练也跑推理，按模型层级归类会失真。一家企业可横跨多列，取决于其产品线覆盖。',
  'scope3':'口径：仅含<b>基础模型、推理框架与中间层、应用厂商</b>。算力与硬件企业不按场景归类——同一颗芯片同时服务编程、客服与科研。一家企业可覆盖多个场景，标记数字即为其跨环节数量。',
  'scope4':'口径：行是<b>玩家模式</b>（卖什么、怎么收费），列是<b>模型层级</b>。<b>拆五列不是按参数量，是按商业形态</b>：前沿闭源卖 API 与订阅，开源权重卖生态与私有化，垂直专用卖结果，端侧小模型卖设备，推理/多模态卖能力溢价。硬件与基础设施不参与模式矩阵，理由见页脚。',
  'note4':'<b>两个值得注意的空格</b>：模型厂商 × 端侧小模型基本由开源阵营占据（闭源前沿厂商很少单独做端侧）；应用厂商 × 前沿闭源高度密集，说明应用层目前仍高度依赖少数几家 API，切换成本与议价权都不在自己手里。',
  'about':'企业按“主营业环节”归类，横跨多个环节的公司（如英伟达、阿里、华为）会在多处出现，用“多环节”标记。模型层级按“该企业主力产品形态”标注；应用场景按“已落地的场景”标注，同样可跨多个场景。<b>“按模型层级”“按应用场景”“按玩家模式”三个视图只收录模型、工具与应用厂商</b>——上游算力与基础设施不参与，因为它们一套硬件同时服务全部模型与场景。归类为编辑判断，非官方口径。',
  'layers':[('01','上游','芯片 · HBM · 光互联 · 服务器 · 电力冷却 · 数据'),('02','中游','基础模型 · 推理引擎 · 编译算子 · 中间层 · Agent'),('03','下游','编程 · 客服 · 知识库 · 内容 · 企业软件 · 消费级')],
  'supportdesc':'开源社区 · 云与数据中心 · 评测合规',
  'SEG':{
   'u1':['上游','AI 芯片 / 加速器'],'u2':['上游','HBM 与 DRAM'],'u3':['上游','晶圆代工与封装'],
   'u4':['上游','光模块与光芯片'],'u5':['上游','服务器与整机'],'u6':['上游','电力与冷却'],
   'u7':['上游','训练数据与标注'],
   'm1':['中游','前沿闭源模型'],'m2':['中游','开源权重模型'],'m3':['中游','垂直 / 端侧模型'],
   'm4':['中游','推理引擎'],'m5':['中游','编译与算子库'],'m6':['中游','中间层与工具'],
   'm7':['中游','Agent 框架'],
   'd1':['下游','编程'],'d2':['下游','客服与工单'],'d3':['下游','知识库与 RAG'],
   'd4':['下游','Agent 与工作流'],'d5':['下游','内容与营销'],'d6':['下游','消费级应用'],
   'd7':['下游','企业软件'],'d8':['下游','科研与垂直行业'],
   's1':['支撑层','开源社区与生态'],'s2':['支撑层','云与数据中心'],'s3':['支撑层','评测与合规']
  },
  'SUPPORT':['s1','s2','s3'],
  'APP_SEGS':['m1','m2','m3','m4','m5','m6','m7','d1','d2','d3','d4','d5','d6','d7','d8'],
  'TECH':[['FT','前沿闭源','卖 API 与订阅 · 最贵'],['OW','开源权重','卖生态与私有化'],['VT','垂直专用','卖结果 · 按任务收费'],['SM','端侧小模型','卖设备 · 低功耗'],['MM','推理 / 多模态','卖能力溢价']],
  'TSHORT':{'FT':'前沿闭源','OW':'开源权重','VT':'垂直专用','SM':'端侧小模型','MM':'推理/多模态'},
  'SCENE':[['编程','第一个跑通的场景'],['企业软件','续约率是验证点'],['知识库','项目多，难量化'],['Agent 与工作流','演示多，可靠性待解'],['内容营销','便宜，效果难归因'],['消费级应用','用户多，ARPU 低'],['科研与垂直','高价值但小众'],['客服与工单','ROI 好算，已规模化']],
  'MODES':[['model','基础模型厂商','卖 token / 订阅','#1b4a75'],['tool','工具与中间层','卖框架 / 服务','#8a6416'],['app','应用厂商','卖席位 / 结果','#a8271f'],['infra','云与算力','卖卡时 / 算力','#5f6b7a'],['part','算力与硬件','卖芯片 / 设备','#2f6f5e']],
  'BLANKS':[],
},
'infra': {
  'slug':'ai-infrastructure-landscape','title':'AI 基础设施产业研究','en':'AI Infra Research',
  'brand':'AI 基础设施产业研究','doc':'AI 基础设施行业观察笔记','docfile':'AI基础设施行业观察笔记.html',
  'tagline':'一份个人整理的行业笔记',
  'intro':'从晶圆封装到液冷供电，把这条产业链拆成 @@SEGN@@ 个环节、@@TOTAL@@ 家企业。<b>供应链图谱含全链条</b>；<b>负载类型</b>、<b>应用场景</b>、<b>玩家模式</b>三个视图覆盖芯片器件、整机集群、软件调度与基础设施服务。点击带绿点的公司名，直达调研报告。',
  'seg':'24','tech':'5','scene':'8',
  'tabs':['供应链图谱','按负载类型','按应用场景','按玩家模式'],
  'scope2':'口径：按<b>算力负载</b>而非按产品规格归类。同一台服务器既能训练也能推理，一家企业可横跨多列，取决于其产品实际服务的负载。列里的数字是有该负载相关产品的企业数，不代表收入结构。',
  'scope3':'口径：按<b>最终算力用途</b>归类。上游器件与中游硬件也会出现在场景中，因为同一批 GPU 和光模块会流向训练、推理、科研等不同用途——这与自动驾驶图谱不同：那里技术等级由整车定义，这里的负载由任务定义，硬件必须参与才看得清全貌。',
  'scope4':'口径：行是<b>玩家模式</b>（卖什么），列是<b>负载类型</b>。<b>拆五列不是等级，是任务</b>：训练看互联与峰值算力，推理看内存带宽与每瓦 token，端侧看功耗，科研看双精度与稳定性。同一家企业的不同产品线会落在不同列。',
  'note4':'<b>两个值得注意的空格</b>：软件与调度 × 边缘推理相对稀薄（端侧多由芯片厂自带工具链闭环）；基础设施服务 × 仿真与科学计算主要靠国家队与超算中心，商业云厂商参与有限。',
  'about':'企业按“主营业环节”归类，横跨多个环节的公司（如英伟达、华为、阿里）会在多处出现，用“多环节”标记。负载类型按“该企业产品实际服务的算力任务”标注；应用场景按“最终算力用途”标注。<b>与自动驾驶图谱的口径差异</b>：那里零部件不进技术等级视图，因为 L2/L4 由整车责任定义；这里硬件必须进负载与场景视图，因为训练/推理的差别恰恰落在芯片、HBM、光模块与液冷上。归类为编辑判断，非官方口径。',
  'layers':[('01','上游','晶圆 · 封装 · HBM · 存储 · 光芯片 · PCB · 电力'),('02','中游','AI 芯片 · 光模块 · 交换 · 服务器 · 液冷 · 框架调度 · 超节点'),('03','下游','智算集群 · 云算力 · 训练 · 推理 · 行业应用')],
  'supportdesc':'电网与绿电 · 数据中心建设 · 标准测试',
  'SEG':{
   'u1':['上游','晶圆代工'],'u2':['上游','先进封装 CoWoS'],'u3':['上游','HBM 与 DRAM'],
   'u4':['上游','企业级存储 / SSD'],'u5':['上游','光芯片与器件'],'u6':['上游','PCB 与铜连接'],
   'u7':['上游','电力与散热设备'],
   'm1':['中游','AI 芯片 GPU / ASIC'],'m2':['中游','光模块'],'m3':['中游','交换芯片与网络'],
   'm4':['中游','服务器整机'],'m5':['中游','液冷系统'],'m6':['中游','推理框架与编译'],
   'm7':['中游','集群调度'],'m8':['中游','超节点整机'],
   'd1':['下游','智算集群'],'d2':['下游','云与算力租赁'],'d3':['下游','模型训练'],
   'd4':['下游','模型推理'],'d5':['下游','行业 AI 应用'],
   's1':['支撑层','电网与绿电'],'s2':['支撑层','数据中心建设'],'s3':['支撑层','标准与测试']
  },
  'SUPPORT':['s1','s2','s3'],
  'APP_SEGS':['m1','m2','m3','m4','m5','m6','m7','m8','d1','d2','d3','d4','d5'],
  'TECH':[['TR','训练','看互联与峰值算力'],['IN','推理','看每瓦 token 产出'],['FT','微调 / 后训练','中等规模，迭代快'],['SI','仿真与科学计算','双精度与稳定性'],['ED','边缘推理','功耗与成本优先']],
  'TSHORT':{'TR':'训练','IN':'推理','FT':'微调','SI':'仿真/HPC','ED':'边缘推理'},
  'SCENE':[['大模型训练','万卡集群，资本密集'],['大模型推理','已占算力支出 55%–70%'],['公有云算力','按卡时出租'],['企业私有化','信创与数据合规驱动'],['科研计算','超算与国家队主导'],['自动驾驶训练','车企与方案商自建'],['具身智能训练','仿真 + 真机数据'],['工业视觉','端侧与边缘推理']],
  'MODES':[['part','芯片与器件厂','卖硅 · 毛利最高','#1b4a75'],['soft','软件与调度','卖利用率 · 开源为主','#8a6416'],['svc','基础设施服务','卖算力与电','#a8271f'],['infra','整机与集群','卖机柜与交付','#5f6b7a']],
  'BLANKS':[],
},
'mobile': {
  'slug':'mobile-internet-landscape','title':'移动互联网产业研究','en':'Mobile Internet Research',
  'brand':'移动互联网产业研究','doc':'移动互联网行业观察笔记','docfile':'移动互联网行业观察笔记.html',
  'tagline':'一份个人整理的行业笔记，含 1983–2026 发展史',
  'intro':'从 1G 语音到 AI 原生入口，把这条产业链拆成 @@SEGN@@ 个环节、@@TOTAL@@ 家企业。<b>供应链图谱含全链条</b>；<b>按业态</b>、<b>按应用场景</b>、<b>按玩家模式</b>三个视图只收录平台、应用与服务厂商。点击带绿点的公司名，直达调研报告。',
  'seg':'24','tech':'5','scene':'8',
  'tabs':['供应链图谱','按业态','按应用场景','按玩家模式'],
  'scope2':'口径：按<b>业态</b>而非按产品形态归类，一家企业可横跨多列，取决于其业务覆盖（比如微信同时是社交通讯、生活服务与工具效率）。上游芯片、终端硬件、云与算力不参与此视图——同一颗芯片、同一台手机会同时服务全部业态，按业态归类会失真。',
  'scope3':'口径：按<b>用户场景</b>归类。上游硬件与网络基础设施不按场景划分——同一条 5G 网络同时承载通讯、购物、支付与游戏。一家企业可覆盖多个场景，标记数字即为其跨环节数量。',
  'scope4':'口径：行是<b>玩家模式</b>（靠什么赚钱），列是<b>业态</b>。<b>拆五列不是按技术代际，是按生意类型</b>：社交通讯卖关系链、内容娱乐卖时长、电商交易卖佣金、生活服务卖履约、工具效率卖订阅。同一家公司的不同业务线会落在不同列。上游器件与网络不参与模式矩阵，理由见页脚。',
  'note4':'<b>两个值得注意的空格</b>：终端与 OS 厂商 × 电商交易基本为空（卖设备的不参与交易抽佣，只通过应用商店收分发费）；网络与算力 × 内容娱乐同样稀薄——流量涨 17.9% 而收入 -1.9%，管道层始终没能分享到内容变现的溢价。',
  'about':'企业按“主营业环节”归类，横跨多个环节的公司（如阿里、腾讯、华为、字节）会在多处出现，用“多环节”标记。业态按“该企业主要的生意类型”标注；应用场景按“用户实际使用的场合”标注，同样可跨多个场景。<b>“按业态”“按应用场景”“按玩家模式”三个视图只收录平台、应用与服务厂商</b>——上游芯片、器件、终端硬件与网络基础设施不参与，因为一套硬件或一张网络同时服务全部业态与场景。归类为编辑判断，非官方口径。发展史详见行业观察笔记第二章。',
  'layers':[('01','上游','网络运营商 · 芯片器件 · 终端整机 · OS · 云算力 · 数据'),('02','中游','应用分发 · 社交 · 内容 · 电商 · 生活服务 · 游戏 · 广告 · 支付 · AI 原生'),('03','下游','即时零售 · 直播短剧 · 云游戏 · 商户 SaaS · 出海 · 下沉与银发')],
  'supportdesc':'数据研究 · 行业组织与监管 · 安全风控',
  'SEG':{
   'u1':['上游','通信运营商'],'u2':['上游','芯片与器件'],'u3':['上游','终端整机'],
   'u4':['上游','移动 OS 与运行时'],'u5':['上游','云与算力 / CDN'],'u6':['上游','训练数据与标注'],
   'm1':['中游','应用商店与分发'],'m2':['中游','社交通讯'],'m3':['中游','内容与短视频'],
   'm4':['中游','电商与零售平台'],'m5':['中游','本地生活与出行'],'m6':['中游','移动游戏'],
   'm7':['中游','广告与营销'],'m8':['中游','支付与清算'],'m9':['中游','AI 原生应用'],
   'd1':['下游','即时零售'],'d2':['下游','直播电商与短剧'],'d3':['下游','云游戏与游戏出海'],
   'd4':['下游','商户服务 SaaS'],'d5':['下游','出海与海外市场'],'d6':['下游','下沉与银发服务'],
   's1':['支撑层','数据与研究'],'s2':['支撑层','行业组织与监管'],'s3':['支撑层','安全与风控']
  },
  'SUPPORT':['s1','s2','s3'],
  'APP_SEGS':['m1','m2','m3','m4','m5','m6','m7','m8','m9','d1','d2','d3','d4','d5','d6'],
  'TECH':[['SOC','社交通讯','卖关系链 · 入口价值最高'],['CON','内容娱乐','卖时长 · 算法分发'],['COM','电商交易','卖佣金与履约'],['LIFE','生活服务','卖本地履约'],['TOOL','工具效率','卖订阅与能力']],
  'TSHORT':{'SOC':'社交通讯','CON':'内容娱乐','COM':'电商交易','LIFE':'生活服务','TOOL':'工具效率'},
  'SCENE':[['即时通讯','用户见顶，但入口价值最高'],['内容消费','短视频占时长第一'],['网络购物','增速回落到个位数'],['本地生活','即时零售 +112.3%'],['移动支付','已成基础设施，饱和'],['移动游戏','稳健增长，出海是增量'],['办公协作','订阅制，中国渗透偏低'],['AI助手','从轻量尝鲜转重度使用']],
  'MODES':[['platform','超级 App 平台','卖流量与生态 · 抽成','#1b4a75'],['vertical','垂直应用商','卖服务 / 商品','#a8271f'],['term','终端与 OS','卖设备与分发','#8a6416'],['infra','网络与算力','卖连接与资源','#5f6b7a'],['support','支撑服务商','卖数据 / 合规 / 清算','#2f6f5e']],
  'BLANKS':[],
},
'space': {
  'slug':'commercial-space-landscape','title':'商用航天与太空通信产业研究','en':'Commercial Space Research',
  'brand':'商用航天与太空通信产业研究','doc':'商用航天与太空通信行业观察笔记','docfile':'商用航天与太空通信行业观察笔记.html',
  'tagline':'一份个人整理的行业笔记',
  'intro':'从火箭发动机到卫星运营，把这条产业链拆成 @@SEGN@@ 个环节、@@TOTAL@@ 家企业。<b>供应链图谱含全链条</b>；<b>按任务类型</b>、<b>应用场景</b>、<b>玩家模式</b>三个视图只收录火箭总装、卫星总装、发射服务、测控运营与应用服务方。点击带绿点的公司名，直达调研报告。',
  'seg':'22','tech':'6','scene':'8',
  'tabs':['供应链图谱','按任务类型','按应用场景','按玩家模式'],
  'scope2':'口径：仅含<b>火箭总装、卫星总装、发射服务、测控运营、应用服务</b>。上游发动机、结构材料、星载芯片、载荷与终端不参与此视图——同一颗 T/R 芯片会同时装进通信星、遥感星和导航星，按任务归类会失真。一家企业可横跨多列，取决于其产品线覆盖。<b>运载火箭统一归入“发射服务”</b>，因为它不按轨道用途分类。',
  'scope3':'口径：仅含<b>火箭总装、卫星总装、发射服务、测控运营、应用服务</b>。上游器件与地面站不按场景归类——同一套地面终端同时服务应急、海事与物联网。一家企业可覆盖多个场景，标记数字即为其跨环节数量。',
  'scope4':'口径：行是<b>玩家模式</b>（靠什么赚钱、担什么责），列是<b>任务类型</b>。<b>拆六列不是按技术代际，是按买单方与资产属性</b>：低轨通信赌规模，低轨遥感已经能赚钱，高轨是存量现金流，导航增强依附北斗，发射服务卖运力，深空与在轨服务是期权。器件与地面站不参与模式矩阵，理由见页脚。',
  'note4':'<b>两个值得注意的空格</b>：民营火箭 × 低轨遥感基本为空（遥感星小，拼车发射更划算，单买一发火箭不经济）；运营商 × 深空与在轨完全为空（这一块还没有商业闭环，付钱的是政府和科研机构）。',
  'about':'企业按“主营业环节”归类，横跨多个环节的公司（如 SpaceX、中国卫星、航天科技集团）会在多处出现，用“多环节”标记。任务类型按“该企业主力产品服务的任务”标注；应用场景按“已落地的场景”标注，同样可跨多个场景。<b>“按任务类型”“按应用场景”“按玩家模式”三个视图只收录火箭总装、卫星总装、发射服务、测控运营与应用服务方</b>——上游器件、材料、载荷与终端不参与，因为一套产品同时服务全部任务与场景。归类为编辑判断，非官方口径。',
  'layers':[('01','上游','发动机 · 结构复材 · 星载芯片 · 平台 · 载荷 · 终端'),('02','中游','火箭总装 · 卫星批产 · 地面站 · 发射 · 测控 · 运营'),('03','下游','遥感 · 导航增强 · 行业通信 · 在轨服务')],
  'supportdesc':'测试认证 · 保险金融 · 院所研发',
  'SEG':{
   'u1':['上游','火箭发动机与动力'],'u2':['上游','火箭结构与复合材料'],'u3':['上游','星载芯片与射频器件'],
   'u4':['上游','卫星平台与姿控'],'u5':['上游','通信载荷与相控阵'],'u6':['上游','遥感载荷与光学'],
   'u7':['上游','地面终端与天线'],'u8':['上游','连接器与电子元器件'],
   'm1':['中游','运载火箭总装'],'m2':['中游','卫星总装与批产'],'m3':['中游','地面站与核心网'],
   'm4':['中游','发射服务与工位'],'m5':['中游','测控与卫星运营'],'m6':['中游','卫星宽带与移动运营'],
   'm7':['中游','卫星物联网运营'],
   'd1':['下游','遥感数据与应用'],'d2':['下游','导航增强与位置服务'],'d3':['下游','卫星通信行业应用'],
   'd4':['下游','在轨服务与太空旅游'],
   's1':['支撑层','测试认证与仿真'],'s2':['支撑层','航天保险与金融'],'s3':['支撑层','院所与研发平台']
  },
  'SUPPORT':['s1','s2','s3'],
  'APP_SEGS':['m1','m2','m4','m5','m6','m7','d1','d2','d3','d4'],
  'TECH':[['LC','低轨通信','星座组网的主战场'],['LO','低轨遥感','最先跑通商业化'],['GEO','高轨通信','存量资产，现金流稳'],['NAV','导航增强','依附北斗做补充'],['LV','发射服务','不按轨道分类'],['DEEP','深空与在轨','远期期权']],
  'TSHORT':{'LC':'低轨通信','LO':'低轨遥感','GEO':'高轨通信','NAV':'导航增强','LV':'发射服务','DEEP':'深空在轨'},
  'SCENE':[['宽带接入','星座规模决定体验'],['手机直连','存量机不换机'],['海事与航空','单价高、需求真'],['应急通信','政府买单'],['卫星物联网','低带宽、大量连接'],['遥感监测','九成靠政府与企业'],['导航增强','厘米级定位'],['国防与政府','最大的单一客户']],
  'MODES':[['soe','国家队 / 央企','拿频轨与订单 · 卖基础设施','#1b4a75'],['rocket','民营火箭','卖运力 · 按发结算','#a8271f'],['satellite','民营卫星','卖平台与载荷','#8a6416'],['operator','运营商','卖连接 · 按套餐','#5f6b7a'],['supplier','器件与终端','卖芯片与终端','#2f6f5e'],['app','数据与应用','卖数据与方案','#6b4a8a']],
  'BLANKS':[],
},
'device': {
  'slug':'smart-hardware-landscape','title':'智能硬件产业研究','en':'Smart Hardware Research',
  'brand':'智能硬件产业研究','doc':'智能硬件行业观察笔记','docfile':'智能硬件行业观察笔记.html',
  'tagline':'一份个人整理的行业笔记',
  'intro':'从主控芯片到整机品牌，把这条产业链拆成 @@SEGN@@ 个环节、@@TOTAL@@ 家企业。<b>供应链图谱含全链条</b>；<b>按品类</b>、<b>按应用场景</b>两个视图只收录品牌商、渠道与支撑服务。点击带绿点的公司名，直达调研报告。',
  'seg':'23','tech':'6','scene':'8',
  'tabs':['供应链图谱','按品类','按应用场景','按玩家模式'],
  'scope2':'口径：仅含<b>品牌商、渠道与支撑服务</b>。上游芯片、光学、传感器、电池、结构件与代工不参与此视图——同一颗蓝牙 SoC 会同时装进耳机、手表和眼镜，按品类归类会失真。一家企业可横跨多列，取决于其产品线覆盖。',
  'scope3':'口径：仅含<b>品牌商、渠道与支撑服务</b>。器件与代工不按场景归类——同一套电池同时服务穿戴、清洁与影像。一家企业可覆盖多个场景，标记数字即为其跨环节数量。',
  'scope4':'口径：行是<b>玩家模式</b>（靠什么赚钱），列是<b>品类</b>。<b>矩阵含全链条</b>，包括芯片与代工——因为“卖部件”和“卖整机”是两种完全不同的生意，放在一起才看得出谁在赚谁的钱。同一家公司的不同业务会落在不同行（如小米既做品牌，也做生态链）。',
  'note4':'<b>两个值得注意的空格</b>：代工与方案 × AI 眼镜仍然很薄（眼镜整机目前主要靠歌尔、立讯这类垂直整合厂，纯代工环节还没成型）；品牌商 × AI 玩具只有个位数玩家，因为这个品类更像内容生意，硬件只是外壳。',
  'about':'企业按“主营业环节”归类，横跨多个环节的公司（如歌尔、小米、华为、立讯）会在多处出现，用“多环节”标记。品类按“该企业主力产品的品类”标注；场景按“已落地的场景”标注，同样可跨多个场景。<b>“按品类”“按应用场景”两个视图只收录品牌商、渠道与支撑服务</b>——上游器件与代工不参与，因为一套产品同时服务全部品类与场景。矩阵视图例外，它按玩家模式分组，含全链条。归类为编辑判断，非官方口径。',
  'layers':[('01','上游','主控 SoC · 视觉芯片 · 光学显示 · 传感器 · 声学 · 电池 · 结构件 · PCB'),('02','中游','清洁电器 · 穿戴音频 · 智能影像 · 智能家居 · AI 眼镜 · 代工 · 方案'),('03','下游','线上渠道 · 线下渠道 · 内容订阅 · 配件售后')],
  'supportdesc':'检测认证 · 标准组织 · 供应链物流',
  'SEG':{
   'u1':['上游','主控 SoC（蓝牙 / Wi-Fi / 音频）'],'u2':['上游','视觉与 AI 芯片'],'u3':['上游','光学与显示模组'],
   'u4':['上游','传感器（光学 / 惯性 / 健康）'],'u5':['上游','声学器件'],'u6':['上游','电池与电源'],
   'u7':['上游','结构件与精密制造'],'u8':['上游','PCB 与被动器件'],'u9':['上游','连接器与通信模组'],
   'm1':['中游','清洁电器品牌'],'m2':['中游','可穿戴与音频品牌'],'m3':['中游','智能影像品牌'],
   'm4':['中游','智能家居品牌'],'m5':['中游','AI 眼镜品牌'],'m6':['中游','ODM / OEM 代工'],
   'm7':['中游','方案商与软件'],
   'd1':['下游','线上渠道与平台'],'d2':['下游','线下渠道与运营商'],'d3':['下游','内容与服务订阅'],
   'd4':['下游','配件与售后'],
   's1':['支撑层','检测认证'],'s2':['支撑层','标准组织'],'s3':['支撑层','供应链与物流']
  },
  'SUPPORT':['s1','s2','s3'],
  'APP_SEGS':['m1','m2','m3','m4','m5','d1','d2','d3','d4'],
  'TECH':[['CLEAN','清洁电器','全球前五全是中国品牌'],['WEAR','可穿戴与音频','存量替换，靠健康功能'],['IMAGE','智能影像','高毛利，天花板低'],['EYE','AI 眼镜','最大变量，也最容易看错'],['HOME','智能家居','品类多、单品小'],['TOY','AI 玩具与其他','起量快，周期短']],
  'TSHORT':{'CLEAN':'清洁电器','WEAR':'穿戴音频','IMAGE':'智能影像','EYE':'AI 眼镜','HOME':'智能家居','TOY':'AI 玩具'},
  'SCENE':[['家庭清洁','国内存量，海外扩张'],['影音娱乐','TWS 与投影的基本盘'],['运动与户外','影像与运动手表'],['健康监测','医疗资质是分水岭'],['办公与学习','眼镜与护眼设备'],['老人与儿童','儿童手表，刚需'],['宠物','喂食器与摄像头'],['车载与出行','前装与后装并存']],
  'MODES':[['brand','品牌商','卖产品与品牌溢价','#1b4a75'],['odms','代工与方案','卖制造与设计','#8a6416'],['chip','芯片与器件','卖部件 · 毛利最高','#2f6f5e'],['plat','渠道与平台','卖流量与分发','#a8271f'],['supp','支撑与服务','卖认证 / 内容 / 物流','#5f6b7a']],
  'BLANKS':[],
},
}

# ---------- 生成 ----------
def parse(raw):
    rows=[]
    for line in raw.strip().split('\n'):
        line=line.strip()
        if not line or line.startswith('#'): continue
        p=line.split('|')
        assert len(p)==6, f'bad row: {line}'
        name,segs,tech,scene,rep,mode=p
        rows.append([name, [x for x in segs.split(',') if x], [x for x in tech.split(',') if x],
                     [x for x in scene.split(',') if x], None if rep=='-' else rep, mode])
    return rows

def jsval(x):
    return json.dumps(x, ensure_ascii=False)

# 少数原始数据里的笔误/跨行业代码，映射到本行业已定义的维度
TECH_FIX = {
  'embodied': {'WR':'HW'},
  'llm': {},
  'infra': {'MM':'IN'},
  'mobile': {},
  'space': {},
  'device': {},
}
SCENE_FIX = {
  'embodied': {'矿区港口':'特种作业'},
  'llm': {'大模型训练':'科研与垂直','大模型推理':'企业软件','公有云算力':'企业软件',
          '端侧推理':'消费级应用','金融':'科研与垂直','医疗健康':'科研与垂直'},
  'infra': {'端侧推理':'工业视觉'},
  'mobile': {},
  'space': {},
  'device': {},
}

def normalize(C, key):
    tf, sf = TECH_FIX[key], SCENE_FIX[key]
    for c in C:
        t = [tf.get(x,x) for x in c[2]]
        c[2] = list(dict.fromkeys(t))          # 去重且保序
        s = [sf.get(x,x) for x in c[3]]
        c[3] = list(dict.fromkeys(s))
    return C

HTML_SKEL = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@@TITLE@@</title>
<style>@@CSS@@</style>
</head>
<body>

<header class="top">
  <div class="top-in">
    <div class="brand"><span class="mark"></span>@@BRAND@@<small>@@EN@@</small></div>
    <label class="search">
      <svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5L14 14"/></svg>
      <input id="q" type="search" placeholder="搜索企业 / 环节…" autocomplete="off">
    </label>
    <a class="top-link" href="#about">关于</a>
  </div>
</header>

<div class="hero">
  <h1>@@TITLE@@</h1>
  <div class="docs">
    <a class="doc-link" href="reports/@@DOCFILE@@">
      <span class="dl-t">@@DOC@@</span>
      <span class="dl-s">@@TAGLINE@@</span>
      <span class="dl-a">阅读 ↗</span>
    </a>
  </div>
  <p>@@INTRO@@</p>
  <div class="stats">
    <div><b id="s1">0</b>覆盖企业</div>
    <div><b id="s2">0<i> 家</i></b>已出调研报告</div>
    <div><b>@@SEGCOUNT@@</b>产业链环节</div>
    <div><b>@@TECHCOUNT@@</b>@@TAB2@@</div>
    <div><b>@@SCENECOUNT@@</b>@@TAB3@@</div>
  </div>
</div>

<div class="tabs">
  <button class="tab on" data-v="chain">@@TAB1@@</button>
  <button class="tab" data-v="tech">@@TAB2@@</button>
  <button class="tab" data-v="scene">@@TAB3@@</button>
  <button class="tab" data-v="mode">@@TAB4@@</button>
  <div class="legend">
    <span><i class="dot"></i>有调研报告</span>
    <span><i class="dot g"></i>暂无报告</span>
  </div>
</div>

<main class="wrap">

  <section class="view on" id="v-chain">
    <div class="chain">
@@LAYERS@@
    </div>
    <div class="support">
      <div class="support-h"><span class="n">04</span><span class="t">支撑层</span><span class="d">@@SUPPORTDESC@@</span></div>
      <div class="support-grid" id="sup"></div>
    </div>
  </section>

  <section class="view" id="v-tech">
    <p class="scope">@@SCOPE2@@</p>
    <div class="grid5" id="techGrid"></div>
  </section>

  <section class="view" id="v-scene">
    <p class="scope">@@SCOPE3@@</p>
    <div class="grid4" id="sceneGrid"></div>
  </section>

  <section class="view" id="v-mode">
    <p class="scope">@@SCOPE4@@</p>
    <div class="matrix" id="modeGrid"></div>
    <p class="scope" style="margin-top:14px;border-left-color:#E24B4A;">@@NOTE4@@</p>
  </section>

  <div class="empty" id="empty">没有匹配的企业，换个关键词试试。</div>
</main>

<footer class="foot" id="about">
  <hr class="rule">
  <p><b>关于这张图。</b>@@ABOUT@@</p>
  <p><b>数据与免责。</b>企业名单基于公开信息整理，用于行业结构展示，不构成任何投资建议；覆盖不代表推荐。报告内容以原稿为准，数据截止各报告标注日期。</p>
</footer>

<script>
const SEG = @@SEG@@;
const TECH = @@TECH@@;
const SCENE = @@SCENE@@;
const SC = @@SC@@;
const TSHORT = @@TSHORT@@;
const APP_SEGS = @@APP_SEGS@@;
const SUPPORT_SEGS = @@SUPPORT@@;
const MODES = @@MODES@@;
const BLANKS = @@BLANKS@@;
const C = @@CDATA@@;

const byReport = (a,b)=> (b[4]?1:0)-(a[4]?1:0);
const isApp = c => c[1].some(s=>APP_SEGS.includes(s));
const modeOf = c => c[5] || null;
const $ = s => document.querySelector(s);
const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const reportCount = C.filter(x=>x[4]).length;
$('#s1').textContent = C.length;
$('#s2').innerHTML = reportCount + '<i> 家</i>';

function chip(c){
  const [n,segs,tech,scene,r] = c;
  const multi = segs.length>1 ? ' multi' : '';
  const badge = segs.length>1 ? `<span class="mc" title="横跨 ${segs.length} 个环节">${segs.length}</span>` : '';
  const inner = esc(n) + badge + (r ? '<span class="ar">↗</span>' : '');
  if(r) return `<a class="chip r${multi}" href="reports/${encodeURIComponent(r)}.html" title="${esc(n)} · 查看调研报告" data-n="${esc(n)}">${inner}</a>`;
  return `<span class="chip${multi}" data-n="${esc(n)}" title="${esc(n)}（暂无调研报告）">${esc(n)}</span>`;
}

const up = [], mid = [], down = [], sup = [];
Object.keys(SEG).forEach(k=>{
  const [layer,name] = SEG[k];
  const list = C.filter(c=>c[1].includes(k)).sort(byReport);
  if(!list.length) return;
  const h = `<div class="seg" data-seg="${k}">
    <div class="seg-h"><span class="st">${name}</span><span class="cnt">${list.length}</span></div>
    <div class="chips">${list.map(chip).join('')}</div>
  </div>`;
  if(SUPPORT_SEGS.includes(k)) sup.push(h);
  else if(layer==='上游') up.push(h);
  else if(layer==='中游') mid.push(h);
  else down.push(h);
});
$('#up').innerHTML = up.join('');
$('#mid').innerHTML = mid.join('');
$('#down').innerHTML = down.join('');
$('#sup').innerHTML = sup.join('');

$('#techGrid').innerHTML = TECH.map(([k,t,s])=>{
  const list = C.filter(c=>isApp(c) && c[2].includes(k)).sort(byReport);
  return `<div><div class="col-h"><div class="t">${t}<span class="cc">${list.length}</span></div><div class="s">${s}</div></div>
    <div class="colbox" data-tech="${k}">${list.map(chip).join('')}</div></div>`;
}).join('');

$('#sceneGrid').innerHTML = SCENE.map(([k,d],i)=>{
  const list = C.filter(c=>isApp(c) && c[3].includes(k)).sort(byReport);
  return `<div class="scene${i===0?' wide':''}" data-scene="${k}"><h3>${k}<span class="cc">${list.length}</span></h3><div class="m">${d}</div>
    <div>${list.map(chip).join('')}</div></div>`;
}).join('');

let mhtml = '<div class="mrow"><div class="mhead"></div>' +
  TECH.map(([k,t,s])=>`<div class="mhead"><div class="ht">${TSHORT[k]}<span class="cc">${C.filter(c=>modeOf(c)&&c[2].includes(k)).length}</span></div><div class="hs">${s}</div></div>`).join('') + '</div>';
MODES.forEach(([mk,mt,ms,col])=>{
  mhtml += `<div class="mrow"><div class="mlab"><div class="mt" style="color:${col}">${mt}</div><div class="ms">${ms}</div></div>`;
  TECH.forEach(([k])=>{
    const blank = BLANKS.find(b=>b[0]===mk && b[1]===k);
    let inner;
    if(blank){
      inner = `<div class="mblank"><b>${blank[2]}</b>${blank[3]}</div>`;
    } else {
      const list = C.filter(c=>modeOf(c)===mk && c[2].includes(k)).sort(byReport);
      inner = list.length ? list.map(chip).join('') : '<span class="mnone">—</span>';
    }
    mhtml += `<div class="mcell">${inner}</div>`;
  });
  mhtml += '</div>';
});
$('#modeGrid').innerHTML = mhtml;

document.querySelectorAll('.tab').forEach(b=>{
  b.onclick = ()=>{
    document.querySelectorAll('.tab').forEach(x=>x.classList.remove('on'));
    b.classList.add('on');
    document.querySelectorAll('.view').forEach(v=>v.classList.remove('on'));
    $('#v-'+b.dataset.v).classList.add('on');
  };
});

if(['#tech','#scene','#chain','#mode'].includes(location.hash)){
  const k = location.hash.slice(1);
  const b = document.querySelector('.tab[data-v="'+k+'"]');
  if(b) b.click();
}

const q = $('#q');
q.addEventListener('input', ()=>{
  const v = q.value.trim().toLowerCase();
  let shown = 0;
  document.querySelectorAll('.chip').forEach(el=>{
    const hit = !v || el.dataset.n.toLowerCase().includes(v);
    el.classList.toggle('hide', !hit);
    if(hit) shown++;
  });
  document.querySelectorAll('.seg, .scene').forEach(el=>{
    const any = [...el.querySelectorAll('.chip')].some(c=>!c.classList.contains('hide'));
    el.classList.toggle('hide', !any);
  });
  document.querySelectorAll('.colbox').forEach(el=>{
    const box = el.closest('div').parentElement;
    const any = [...el.querySelectorAll('.chip')].some(c=>!c.classList.contains('hide'));
    if(box) box.style.opacity = any ? 1 : .35;
  });
  $('#empty').style.display = (v && shown===0) ? 'block' : 'none';
});
</script>
</body>
</html>
'''

def build(key, cfg):
    C = normalize(parse(RAW[key]), key)
    segn = len(cfg['SEG'])
    layers = '\n'.join(
      f'''      <div class="layer">
        <div class="layer-h"><span class="n">{n}</span><span class="t">{t}</span><span class="d">{d}</span></div>
        <div id="{i}"></div>
      </div>''' for (n,t,d),i in zip(cfg['layers'],['up','mid','down']))
    rep = {
      '@@TITLE@@':cfg['title'],'@@BRAND@@':cfg['brand'],'@@EN@@':cfg['en'],
      '@@DOC@@':cfg['doc'],'@@DOCFILE@@':cfg['docfile'],'@@TAGLINE@@':cfg['tagline'],
      '@@INTRO@@':cfg['intro'].replace('@@SEGN@@',str(segn)).replace('@@TOTAL@@',f'<span id="total">{len(C)}</span>'),
      '@@SEGCOUNT@@':str(segn),'@@TECHCOUNT@@':str(len(cfg['TECH'])),'@@SCENECOUNT@@':str(len(cfg['SCENE'])),
      '@@TAB1@@':cfg['tabs'][0],'@@TAB2@@':cfg['tabs'][1],'@@TAB3@@':cfg['tabs'][2],'@@TAB4@@':cfg['tabs'][3],
      '@@LAYERS@@':layers,'@@SUPPORTDESC@@':cfg['supportdesc'],
      '@@SCOPE2@@':cfg['scope2'],'@@SCOPE3@@':cfg['scope3'],'@@SCOPE4@@':cfg['scope4'],
      '@@NOTE4@@':cfg['note4'],'@@ABOUT@@':cfg['about'],
      '@@CSS@@':CSS,
      '@@SEG@@':jsval(cfg['SEG']),'@@TECH@@':jsval(cfg['TECH']),
      '@@SCENE@@':jsval(cfg['SCENE']),
      '@@SC@@':jsval({k:k for k,_ in cfg['SCENE']}),
      '@@TSHORT@@':jsval(cfg['TSHORT']),'@@APP_SEGS@@':jsval(cfg['APP_SEGS']),
      '@@SUPPORT@@':jsval(cfg['SUPPORT']),'@@MODES@@':jsval(cfg['MODES']),
      '@@BLANKS@@':jsval(cfg['BLANKS']),'@@CDATA@@':jsval(C),
    }
    out = HTML_SKEL
    for k,v in rep.items():
        out = out.replace(k,v)
    # intro 里的 total span 需要 JS 同步（保持和原站一致）
    out = out.replace("$('#s1').textContent = C.length;", "$('#total').textContent = C.length;\n$('#s1').textContent = C.length;")
    return out, C

def main():
    os.makedirs(OUT, exist_ok=True)
    for key,cfg in SITES.items():
        d = os.path.join(OUT, cfg['slug'])
        os.makedirs(os.path.join(d,'reports','md'), exist_ok=True)
        os.makedirs(os.path.join(d,'tools'), exist_ok=True)
        text, C = build(key,cfg)
        open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(text)
        # 报告链接清单
        reps = sorted({c[4] for c in C if c[4]})
        print(f"{cfg['slug']}: {len(C)} 家企业 / {len(cfg['SEG'])} 环节 / {len(reps)} 份研报")
        for r in reps: print('   -',r)
        open(os.path.join(d,'.reports.json'),'w',encoding='utf-8').write(json.dumps(reps,ensure_ascii=False,indent=1))
    print('done')

if __name__=='__main__':
    main()
