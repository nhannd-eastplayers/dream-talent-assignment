"""Maintainer utility to regenerate application-owned JSON Schemas."""
from core import ROOT, write

STR = {'type': 'string', 'minLength': 1}
TEXT = {'type': 'string'}
IDS = {'type': 'array', 'items': STR, 'uniqueItems': True}
STATUS = {'enum': ['observed', 'inferred', 'proposed']}
VERIFY = {'enum': ['verified', 'partial', 'blocked', 'unverified']}

def obj(properties, required=None):
    return {'type': 'object', 'properties': properties, 'required': list(properties) if required is None else required, 'additionalProperties': False}

def array(item):
    return {'type': 'array', 'items': item}

def save(name, schema):
    schema['$schema'] = 'https://json-schema.org/draft/2020-12/schema'
    write(ROOT / name, schema)

claim = {'id': {'type': 'string', 'pattern': '^[A-Za-z][A-Za-z0-9_-]*$'}, 'name': STR, 'description': STR,
         'status': STATUS, 'verificationState': VERIFY, 'evidenceIds': IDS, 'rationale': TEXT}
record = dict(claim)
record.update({k: IDS for k in ['actorIds', 'entityIds', 'workflowIds', 'stepIds', 'businessRuleIds', 'openQuestionIds', 'dependsOn', 'featureIds']})
record.update({k: array(STR) for k in ['entryPages', 'preconditions', 'inputs', 'outputs', 'mainFlow', 'alternativeFlows']})
record_schema = obj(record, list(claim))
feature_required = list(claim) + ['actorIds', 'entryPages', 'preconditions', 'inputs', 'outputs', 'mainFlow', 'alternativeFlows', 'entityIds', 'businessRuleIds', 'dependsOn', 'openQuestionIds', 'workflowIds']
save('schemas/knowledge.schema.json', obj({k: obj(claim) if k == 'system' else array(obj(record, feature_required) if k == 'features' else record_schema) for k in ['system', 'modules', 'actors', 'features', 'workflows', 'steps', 'entities', 'businessRules', 'openQuestions']}))
req = {k: v for k, v in claim.items() if k not in ('name', 'description')}
req.update({'featureId': STR, 'type': {'enum': ['functional', 'nonfunctional', 'data', 'constraint']}, 'statement': STR,
    **{k: IDS for k in ['actorIds', 'entityIds', 'dependsOn', 'evidenceIds', 'openQuestionIds']},
    **{k: array(STR) for k in ['preconditions', 'mainFlow', 'alternativeFlows']},
    'acceptanceCriteria': {'type': 'array', 'items': STR, 'minItems': 1}})
save('schemas/requirements.schema.json', array(obj(req)))
evidence = {'id': STR, 'sourceType': {'enum': ['browser', 'document', 'fixture', 'http', 'search']}, 'url': {'type': 'string', 'format': 'uri'},
    'capturedAt': {'type': 'string', 'format': 'date-time'}, 'pageTitle': TEXT, 'excerpt': STR, 'locator': STR,
    'snapshotPath': STR, 'screenshotPath': STR, 'action': STR, 'result': STR, 'contentHash': {'type': 'string', 'pattern': '^[a-f0-9]{64}$'}}
save('schemas/evidence.schema.json', array(obj(evidence, [k for k in evidence if k not in ('snapshotPath', 'screenshotPath')])))
node = {'type': 'object', 'required': ['id', 'type'], 'properties': {'id': STR, 'type': {'enum': ['System', 'Module', 'Actor', 'Feature', 'Requirement', 'Workflow', 'Step', 'Entity', 'BusinessRule', 'Evidence', 'OpenQuestion']}}}
edge = obj({'id': STR, 'source': STR, 'target': STR, 'type': {'enum': ['CONTAINS', 'USES', 'HAS_REQUIREMENT', 'INCLUDES', 'INVOLVES', 'SUPPORTED_BY', 'DEPENDS_ON', 'GOVERNED_BY', 'RELATES_TO']}, 'status': STATUS, 'rationale': STR})
save('schemas/graph.schema.json', obj({'nodes': array(node), 'edges': array(edge)}))
state = {'enum': ['pending', 'running', 'completed', 'partial', 'failed', 'blocked']}
stage = obj({'state': state, 'inputHash': TEXT, 'inputFiles': {'type': 'object', 'additionalProperties': STR}, 'artifacts': {'type': 'object', 'additionalProperties': STR}, 'updatedAt': {'type': 'string', 'format': 'date-time'}, 'errors': array(STR)})
from core import STAGES
save('schemas/run.schema.json', obj({'id': STR, 'status': state, 'createdAt': {'type': 'string', 'format': 'date-time'}, 'updatedAt': {'type': 'string', 'format': 'date-time'},
    'inputHash': STR, 'upstreamVersions': {'type': 'object'}, 'stopReason': TEXT, 'errors': array(STR), 'stages': obj({k: stage for k in STAGES})}))
config = {'url': {'type': 'string', 'format': 'uri'}, 'language': STR, 'allowedOrigins': {'type': 'array', 'items': {'type': 'string', 'format': 'uri'}, 'minItems': 1, 'uniqueItems': True},
    'allowMutations': {'const': False}, 'allowLocalFixture': {'type': 'boolean'}, 'outputDirectory': STR}
for key, maximum in [('maxPages', 100), ('maxDepth', 10), ('maxActionsPerPage', 30), ('maxRuntimeMinutes', 120), ('maxRepairIterations', 2), ('requestDelayMs', 10000)]:
    config[key] = {'type': 'integer', 'minimum': 0 if key in ('maxDepth', 'maxActionsPerPage', 'maxRepairIterations', 'requestDelayMs') else 1, 'maximum': maximum}
save('config/schema.json', obj(config))
