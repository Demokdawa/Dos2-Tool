from lxml import etree

tree = etree.parse("Shout_Description.lsx")

list = ["Shout_AS_ResetAp_Description", "Shout_AS_SourceAp_Description", "Shout_RecoverArmour_Description"]

# unused = (tree.find(".//node[@id='TranslatedStringKey']/attribute[@value='Shout_AS_ResetAp_Description']"))
# unused.getparent().getparent().remove(unused)
# tree.write("out.xml")

# for node in tree.xpath(".//node[@id='TranslatedStringKey']/attribute[@id='UUID']/@value"):
    # print(node.index(child))
        #print(node)
        #print('delete the whole bloc')
        #node.getparent().remove(node)


for node in tree.find(".//node[@id='TranslatedStringKey']//attribute[@value='Shout_AS_ResetAp_Description']").getparent():
    print(node)

# toremove = tree.find(".//node[@id='TranslatedStringKey']//attribute[@value='Shout_AS_ResetAp_Description']").getparent()
# toremove.getparent().remove(toremove)
# tree.write("out.xml")

# (".//node[@id='TranslatedStringKey']/attribute[@id='UUID']/@value")

for string in list:
    if tree.find(".//node[@id='TranslatedStringKey']//attribute[@value='{}']".format(string)):
        to_remove = tree.find(".//node[@id='TranslatedStringKey']//attribute[@value='{}']".format(string)).getparent()
        to_remove.getparent().remove(to_remove)
tree.write("out.xml")

