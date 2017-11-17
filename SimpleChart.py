from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart


class MyBarChartDrawing(Drawing):
    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        self.add(HorizontalBarChart(), name='chart')

        self.add(String(200, 180, 'TEST CHART'), name='title')
        self.chart.x = 20
        self.chart.y = 20
        self.chart.width = self.width - 20
        self.chart.height = self.height - 40

        self.title.fontName = 'Helvetica-Bold'
        self.title.fontSize = 12

        self.chart.data = [[100, 150, 200, 235, 400, 15]]


if __name__ == '__main__':
    MyBarChartDrawing().save(formats=['gif', 'png', 'jpg', 'pdf'], outDir='.', fnRoot='barchart')