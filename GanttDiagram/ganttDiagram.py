import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
from matplotlib.dates import MonthLocator, DateFormatter


tasks = [
    ["Skrive introduksjonsdelen av rapporten", "1/2/2025", "1/31/2025", 22],
    ["Skrive teoridelen av rapporten", "1/2/2025", "2/14/2025", 32],
    ["Lage overordnet prosjektplan", "1/2/2025", "1/31/2025", 22],
    ["Opprette Github-organisasjon og repository", "1/2/2025", "1/31/2025", 22],
    ["Forbered ressurser (Azure, OpenAI API-nøkkel)", "1/2/2025", "1/31/2025", 22],
    ["Gjennomgå og diskuter Capgemini kravspesifikasjon", "2/3/2025", "2/14/2025", 10],
    ["Lage egen kravspesifikasjon", "2/3/2025", "2/28/2025", 20],
    ["Designe wireframe for GUI", "2/3/2025", "2/28/2025", 20],
    ["Utarbeide klassediagram for backend", "2/3/2025", "2/28/2025", 20],
    ["Opprette kanban-tavle og legge inn funksjoner", "2/3/2025", "2/28/2025", 20],
    ["Opprette et .Net prosjekt", "2/3/2025", "2/28/2025", 20],
    ["Implementer GUI (uten funksjonalitet)", "2/17/2025", "3/14/2025", 20],
    ["Integrere GUI med backend", "3/14/2025", "5/15/2025", 45],
    ["Implementere kjernefunksjonalitet", "2/17/2025", "4/11/2025", 40],
    ["Konvertere rapporten til LaTeX", "2/17/2025", "5/15/2025", 64],
    ["Dokumenetere API", "2/17/2025", "5/15/2025", 64],
    ["Skrive konklusjonsdelen av rapporten", "3/3/2025", "4/30/2025", 43],
    ["Skrive diskusjonsdelen av rapporten", "3/17/2025", "5/21/2025", 48],
    ["Diskutere og vurdere bonuskrav", "4/1/2025", "4/30/2025", 22],
    ["Brukertesting", "4/1/2025", "4/30/2025", 22],
    ["Enhetstesting, integrasjonstesting og E2E-testing", "2/17/2025", "4/30/2025", 53],
    ["Skrive prosessdokumentasjon", "1/2/2025", "4/30/2025", 85],
    ["Finjustere rapporten", "4/30/2025", "5/16/2025", 13],
    ["Lag innlegg for EXPO", "4/30/2025", "5/23/2025", 18],
    ["Planlegging av presentasjon på EXPO", "4/30/2025", "5/30/2025", 23],
]


df = pd.DataFrame(tasks, columns=["Task", "Start", "Finish", "Duration"])
df["Start"] = pd.to_datetime(df["Start"])
df["Finish"] = pd.to_datetime(df["Finish"])
df = df.sort_values("Start")


month_colors = {
    1: "#A6CEE3", 2: "#B2DF8A", 3: "#FDBF6F", 4: "#CAB2D6", 5: "#FB9A99"
}

fig, ax = plt.subplots(figsize=(15, 10))

for i, row in enumerate(df.itertuples()):
    start = row.Start
    duration = row.Duration
    month = start.month
    color = month_colors.get(month, "#CCCCCC")
    ax.barh(i, duration, left=start, color=color, height=0.8)


ax.set_yticks(range(len(df)))
ax.set_yticklabels(df["Task"], fontsize=9)
ax.invert_yaxis()

ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter('%b %Y'))
plt.xticks(rotation=45, ha='right', fontsize=9)

ax.set_xlim(pd.to_datetime('2025-01-01'), pd.to_datetime('2025-06-01'))

ax.set_title("Gantt-diagram - Prosjektplan 2025", fontsize=14, pad=20)

legend_elements = [Patch(facecolor=color, label=label) for color, label in zip(
    month_colors.values(),
    ["Januar", "Februar", "Mars", "April", "Mai"]
)]
ax.legend(handles=legend_elements, title='Startmåned',
          loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=5)

plt.tight_layout()
plt.subplots_adjust(bottom=0.2)  # Should be 'bottom'

plt.savefig("gantt_diagram_med_måneder.png", dpi=300, bbox_inches='tight')
plt.show()