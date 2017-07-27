import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.AnaTools.osuAnalysis_cfi import collectionMap
from OSUT3Analysis.JoshAnalyzer.EventSelections import *
from OSUT3Analysis.JoshAnalyzer.HistogramDefinitions import *

process = cms.Process("demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,"80X_mcRun2_asymptotic_2016_v3","")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.categories.append('DebugNotes')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",

    fileNames = cms.untracked.vstring(
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_101.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_102.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_103.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_104.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_105.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_106.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_107.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_108.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_109.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_110.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_111.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_112.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_113.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_114.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_115.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_116.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_117.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_118.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_119.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_120.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_121.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_122.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_123.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_124.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_125.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_126.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_127.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_128.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_129.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_130.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_131.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_132.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_133.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_134.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_135.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_136.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_137.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_138.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_139.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_140.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_141.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_142.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_143.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_144.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_145.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_146.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_147.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_148.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_149.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_150.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_151.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_152.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_153.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_154.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_155.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_156.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_157.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_158.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_159.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_160.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_161.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_162.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_163.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_164.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_165.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_166.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_167.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_168.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_169.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_170.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_171.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_172.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_173.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_174.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_175.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_176.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_177.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_178.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_179.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_180.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_181.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_182.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_183.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_184.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_185.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_186.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_187.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_188.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_189.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_190.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_191.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_192.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_193.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_194.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_195.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_196.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_197.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_198.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_199.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_200.root",

    ),
)

weights = cms.VPSet (
#    cms.PSet (
#        inputCollections = cms.vstring("muons"),
#        inputVariable = cms.string("pt")
#    ),
#    cms.PSet (
#        inputCollections = cms.vstring("eventvariables"),
#        inputVariable = cms.string("muTrackInvMass"),
#    )
)

variableProducer = []
variableProducer.append("caloDepTrkCone")

process.TFileService = cms.Service("TFileService", 
    fileName = cms.string("histoTracksDemo100.root")
)

histograms = cms.VPSet(
    muonPlots,
    trackPlots,
    massPlot,
    evtVarPlots,
)

add_channels (process, [trkZeroMissingHitsECalDep02], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkOneMissingHitsECalDep02], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkTwoMissingHitsECalDep02], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkThreeMissingHitsECalDep02], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkZeroMissingHitsECalDep20], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkOneMissingHitsECalDep20], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkTwoMissingHitsECalDep20], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkThreeMissingHitsECalDep20], histograms, weights, [], collectionMap, variableProducer, False)
