# coding: utf-8

"""
    api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from upstudy_py_sdk.models.solver_self_simple_response import SolverSelfSimpleResponse

class TestSolverSelfSimpleResponse(unittest.TestCase):
    """SolverSelfSimpleResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SolverSelfSimpleResponse:
        """Test SolverSelfSimpleResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SolverSelfSimpleResponse`
        """
        model = SolverSelfSimpleResponse()
        if include_optional:
            return SolverSelfSimpleResponse(
                input = '',
                solution = upstudy_py_sdk.models.solver/solution.solver.Solution(
                    block_name = upstudy_py_sdk.models.block_name.block_name(), 
                    results = [
                        upstudy_py_sdk.models.solver/step.solver.Step(
                            children = [
                                upstudy_py_sdk.models.solver/step.solver.Step(
                                    description = upstudy_py_sdk.models.description.description(), 
                                    image_url = '', 
                                    latex = '', )
                                ], 
                            description = upstudy_py_sdk.models.description.description(), 
                            image_url = '', 
                            latex = '', )
                        ], 
                    solution_name = upstudy_py_sdk.models.solution_name.solution_name(), )
            )
        else:
            return SolverSelfSimpleResponse(
        )
        """

    def testSolverSelfSimpleResponse(self):
        """Test SolverSelfSimpleResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
