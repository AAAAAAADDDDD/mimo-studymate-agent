# mimo-studymate-agent
一个面向国际学生的 AI 学习资料处理 Agent：上传课程文字、PPT 导出的文本、访谈 transcript 或截图 OCR 文本后，系统会自动完成：
资料清洗与结构化
中英双语学习笔记
重点概念解释
课堂概念到案例的映射
Quiz 练习题生成
Token 使用记录与成本估算
本项目适合用于 Xiaomi MiMo Orbit 100T Token 计划申请，因为它有明确的 Agent 工作流、真实的学习场景、高频 token 消耗需求，以及可持续迭代方向。
核心技术
Frontend: Streamlit
Agent orchestration: Python modular pipeline
LLM 调用: LiteLLM + Xiaomi MiMo
Default model: `xiaomi\_mimo/mimo-v2-flash`
Storage: Local JSON logs
安装
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```
设置 API Key
```bash
export XIAOMI\_MIMO\_API\_KEY="your\_api\_key\_here"
```
Windows PowerShell:
```powershell
$env:XIAOMI\_MIMO\_API\_KEY="your\_api\_key\_here"
```
运行
```bash
streamlit run app.py
```
使用方式
在左侧选择学习任务类型
粘贴课程文本、transcript、PPT OCR 文本或案例材料
点击 Generate
查看 Agent 输出的结构化结果与 token 使用记录
项目结构
```text
mimo\_studymate\_agent/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── data/
│   └── sample\_lecture.txt
└── src/
    ├── agents.py
    ├── mimo\_client.py
    ├── prompt\_templates.py
    └── storage.py
```
Roadmap
[ ] 加入 PDF / PPTX 文件解析
[ ] 加入图片 OCR 与多模态模型支持
[ ] 加入 RAG，支持课程周次资料检索
[ ] 加入学习进度记忆与错题本
[ ] 加入一键导出 Word / PDF
[ ] 加入团队学习空间
